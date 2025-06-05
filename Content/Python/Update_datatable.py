import os
import csv
import urllib.request
import unreal

# === User variables ===

GOOGLE_SHEET_CSV_URL = (
    'https://docs.google.com/spreadsheets/d/1hJBj66-qGNoDCeqAC5apP5ay6p4Z3EfcQX9aJWxlchI/export?format=csv&id=1hJBj66-qGNoDCeqAC5apP5ay6p4Z3EfcQX9aJWxlchI&gid=0'
)

project_dir = unreal.SystemLibrary.get_project_directory()
csv_relative_path = 'Content/BP/Lenguaje/csv Loop Island.csv'
CSV_SAVE_PATH = os.path.join(project_dir, csv_relative_path).replace('\\', '/')

# Path to the DataTable asset in Content Browser (no file extension)
DATA_TABLE_ASSET_PATH = '/Game/BP/Lenguaje/LenguajeDataTable'
DATA_TABLE_NAME = 'LenguajeDataTable'
ROW_STRUCT_PATH = '/Game/BP/Lenguaje/LenguajeStruct.LenguajeStruct'


# === Functions ===

def fetch_csv_data(url):
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    reader = csv.DictReader(lines)
    data = []
    for row in reader:
        clean_row = {k: v for k, v in row.items() if k}
        data.append(clean_row)
    return data


def save_as_csv(data, filename):
    if not data:
        unreal.log_warning("No data to save!")
        return False

    fieldnames = list(data[0].keys())

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            filtered_row = {k: row.get(k, '') for k in fieldnames}
            writer.writerow(filtered_row)
    return True


def my_reimport():
    try:
        # Prepare task
        task = unreal.AssetImportTask()
        task.filename = CSV_SAVE_PATH
        task.destination_path = DATA_TABLE_ASSET_PATH.rsplit('/', 1)[0]
        task.destination_name = DATA_TABLE_NAME
        task.replace_existing = True
        task.automated = True
        task.save = True

        # Load row struct
        row_struct = unreal.load_object(None, ROW_STRUCT_PATH)
        if not row_struct:
            unreal.log_error(f"❌ Could not load row struct at: {ROW_STRUCT_PATH}")
            return False

        # Set up CSV factory
        csv_factory = unreal.CSVImportFactory()
        import_settings = unreal.CSVImportSettings()
        import_settings.import_row_struct = row_struct
        csv_factory.automated_import_settings = import_settings

        task.factory = csv_factory

        # Import
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([task])

        if task.imported_object_paths:
            unreal.log(f"✅ Reimported: {task.imported_object_paths}")
            return True
        else:
            unreal.log_error("❌ Nothing was reimported. Check if CSV path and DataTable name are correct.")
            return False

    except Exception as e:
        unreal.log_error(f"Exception during reimport: {e}")
        return False


# === Main ===

def main():
    unreal.log("🚀 Starting Google Sheets CSV fetch and DataTable update...")

    data = fetch_csv_data(GOOGLE_SHEET_CSV_URL)
    unreal.log(f"📥 Fetched {len(data)} rows from Google Sheets.")

    saved = save_as_csv(data, CSV_SAVE_PATH)
    if not saved:
        unreal.log_error("❌ Failed to save CSV file.")
        return

    unreal.log(f"💾 CSV saved to {CSV_SAVE_PATH}")

    success = my_reimport()
    if success:
        unreal.log("✅ DataTable reimport successful.")
    else:
        unreal.log_error("❌ DataTable reimport failed.")

    unreal.log("🏁 Script finished.")


if __name__ == "__main__":
    main()
