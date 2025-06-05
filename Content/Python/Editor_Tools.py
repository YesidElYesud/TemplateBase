import unreal
import os

menu_owner = "DataTableUpdater"
tool_menus = unreal.ToolMenus.get()
owning_menu_name = "LevelEditor.LevelEditorToolBar.PlayToolBar"
project_directory = unreal.SystemLibrary.get_project_directory()
python_code_path = os.path.join(project_directory, 'Scripts', 'Update_datatable.py').replace("\\", "/")

@unreal.uclass()
class DataTableToolbarEntry(unreal.ToolMenuEntryScript):
    def init_as_toolbar_button(self):
        self.data.menu = owning_menu_name
        self.data.advanced.entry_type = unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON
        self.data.icon = unreal.ScriptSlateIcon("EditorStyle", "MaterialEditor.CameraHome")
        self.data.advanced.style_name_override = "CalloutToolbar"

def Run():
    entry = DataTableToolbarEntry()
    entry.init_as_toolbar_button()
    entry.init_entry(
        menu_owner,
        owning_menu_name,
        "",
        "updateDataTableEntry",
        "DataTable Tools",
        "Update DataTable from Google Sheets"
    )

    sub_menu = tool_menus.register_menu(
        owning_menu_name + ".updateDataTableEntry",
        "",
        unreal.MultiBoxType.MENU,
        False
    )

    # Call external script
    command_code = f'exec(open(r"{python_code_path}").read())'

    sub_entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner,
        "UpdateDataTable",
        "Update DataTable from Google Sheets",
        "Fetch and import CSV from Google Sheets",
        unreal.ToolMenuStringCommandType.PYTHON,
        "",
        command_code
    )

    sub_menu.add_menu_entry("", sub_entry)

    toolbar = tool_menus.extend_menu(owning_menu_name)
    toolbar.add_menu_entry_object(entry)
    tool_menus.refresh_all_widgets()

Run()
