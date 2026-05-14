# Building the Windows installer

This repo already contains an NSIS installer script at `windows/install.nsi`. To package the current checkout into `windows/pithos_installer.exe`:

1. Install [NSIS](https://nsis.sourceforge.io/Download).
2. Make sure `makensis.exe` is available in your `PATH`.
3. From a Windows command prompt, run:

   ```bat
   windows\build_installer.bat
   ```

The installer includes the application files from this repository (`data`, `pithos`, `pithos.pyw`, and `pithos.bat`) and can optionally download/install the legacy runtime dependencies declared in `install.nsi`.

## Before uploading publicly

Do **not** include personal runtime data in public releases:

- `%APPDATA%\Pithos\pithos.ini`
- debug logs
- screenshots/logs containing account details or auth tokens

The generated installer should come from a clean checkout of the repo, not from a copied installed profile folder.
