# TemplateBase
Plantilla base para proyectos en Unreal Engine 5.5 que sirve para GameJams

## 🎯 Propósito
Establecer convenciones claras para nombrar variables, clases, Blueprints y otros assets en Unreal Engine con el fin de mantener el código y el contenido organizado, legible y escalable.

---

## 📂 Convenciones Generales

- Usa **PascalCase** para nombres de clases, estructuras y assets.
- Usa **camelCase** para variables y funciones.
- Prefija los nombres de assets con un identificador del tipo (ej: `BP_` para Blueprints).
- No uses espacios, acentos o caracteres especiales (usa `_` para separar términos si es necesario).
- Sé descriptivo pero conciso.

---

## 🧱 Prefijos por Tipo de Asset

| Tipo de Asset          | Prefijo   | Ejemplo                  |
|------------------------|-----------|--------------------------|
| Blueprint Class        | `BP_`     | `BP_PlayerCharacter`     |
| Material               | `M_`      | `M_WoodOak`              |
| Material Instance      | `MI_`     | `MI_WoodOak_01`          |
| Static Mesh            | `SM_`     | `SM_Table_Round`         |
| Skeletal Mesh          | `SK_`     | `SK_Enemy_Goblin`        |
| Texture                | `T_`      | `T_WoodOak_D`            |
| Animation              | `A_`      | `A_RunForward`           |
| Sound Cue              | `SC_`     | `SC_Explosion`           |
| Sound Wave             | `S_`      | `S_Explosion01`          |
| Particle System        | `P_`      | `P_SmokeTrail`           |
| Niagara System         | `NS_`     | `NS_MagicBurst`          |
| User Interface (Widget)| `WBP_`    | `WBP_MainMenu`           |
| Data Table             | `DT_`     | `DT_ItemStats`           |
| Enum                   | `E_`      | `E_ItemType`             |
| Curve                  | `Curve_`  | `Curve_PlayerSpeed`      |

---

## 🧾 Variables

### Tipos Básicos (C++ y Blueprint)

| Tipo          | Prefijo | Ejemplo              |
|---------------|---------|----------------------|
| Boolean       | `b`     | `bIsDead`            |
| Integer       | `i`     | `iScore`             |
| Float         | `f`     | `fSpeed`             |
| FString       | `Str`   | `StrPlayerName`      |
| FVector       | `v`     | `vDirection`         |
| Rotator       | `Rot`   | `RotSpawnAngle`      |
| Actor         | `Actor` | `ActorTarget`        |
| Component     | `Comp`  | `CompMesh`           |

> **Nota:** En Blueprints se puede omitir el prefijo si se hace uso correcto de categorías y comentarios, pero se recomienda su uso en proyectos grandes o en colaboración.

---

## 🧩 Funciones y Eventos

- Usa **camelCase**: `updateHealthBar`, `onPlayerDeath`.
- Empieza funciones booleanas con verbos como `is`, `has`, `can`:  
  - `isAlive()`, `hasKeyItem()`, `canJump()`.
