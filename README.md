# DD Palette Forge - GitHub starter

## Recommended flow

1. Enable **GitHub Pages** for this repository from the `main` branch / repository root.
2. Put the app at `index.html`.
3. Add hero assets under:

```text
library/
  vanilla/
    vestal/
      vestal_A/
        ...
      vestal_B/
        ...
  mods/
    lamia/
      lamia_A/
        ...
```

A skin folder may contain nested `anim/` folders. The catalog builder recursively includes:

- `.png`
- `.skel`
- `.atlas`

## Automatic catalog

`tools/build_catalog.py` scans `library/` and creates:

```text
library/index.json
```

The included GitHub Action runs this script whenever `library/**` changes and commits the updated catalog.

## Palette Forge connection

Inside Palette Forge:

1. Open **GitHub** in the top menu.
2. Enter:
   - Owner: your GitHub username
   - Repository: repository name
   - Branch: `main`
   - Mode: **GitHub Pages**
3. Click **Gerar URL**.
4. Click **Testar catálogo**.
5. Click **Salvar**.

For a repo named `dd-palette-forge` owned by `murizz`, the Pages catalog URL would be:

```text
https://murizz.github.io/dd-palette-forge/library/index.json
```

## Important: game assets

Do not redistribute copyrighted base-game or mod assets unless you have permission to do so. A safer public release is to host metadata/templates for copyrighted content and let users import original game files locally. Assets from mod authors should only be mirrored with their permission.
