# Building the Windows installer

This repo already contains an NSIS installer script at `windows/install.nsi`. To package the current checkout into `windows/pithos_installer.exe`:

1. Install [NSIS](https://nsis.sourceforge.io/Download).
2. Make sure `makensis.exe` is available in your `PATH`.
3. From a Windows command prompt, run:

   ```bat
   windows\build_installer.bat
   ```

The installer includes the application files from this repository (`data`, `pithos`, `pithos.pyw`, and `pithos.bat`) and can optionally download/install the legacy runtime dependencies declared in `install.nsi`.

## Large dependencies

The required Python and GStreamer runtime installers are too large to store in git. Their filenames, download URLs, and optional offline workflow are documented in `windows/DEPENDENCIES.md`.

## Before uploading publicly

Build from a clean repository checkout, not from a copied installed profile folder. The installer script only packages repository files, but you should still verify that your public release does **not** include private runtime data:

- `%APPDATA%\Pithos\pithos.ini`
- `%APPDATA%\Pithos\pithos.log`
- other debug logs
- screenshots/logs containing account details or auth tokens

The repository `.gitignore` also excludes the common local config, log, cache, and generated installer files so they are harder to commit by accident.
