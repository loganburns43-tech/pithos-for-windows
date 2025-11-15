Pithos for Windows
=============

Pithos is a native Pandora Radio client for ~~Linux~~ Windows. It's much more lightweight than the Pandora.com web client.

**NOTE** This project is no longer maintained. Upstream [Pithos](https://github.com/pithos/pithos) is actively developed however does not directly support Windows. If you would like to use Pithos on Windows your best chance is probably using the Linux version on Windows via [WSL](https://docs.microsoft.com/en-us/windows/wsl/about).


Installation
-----------
Newest release can be found [here](https://github.com/TingPing/pithos-for-windows/releases) and read notes below.

64bit users can just download this [zip](https://github.com/TingPing/pithos-for-windows/archive/master.zip) and extract it, though 64bit isn't recommended and you will have to manage the dependencies yourself.

See [redist.txt](https://github.com/TingPing/pithos-for-windows/blob/master/windows/redist.txt) for optional plugin requirements.

Updating an existing install
----------------------------

If you already have a working copy (for example, the layout shown in the screenshots above with `Pithos.exe`, `pithos.bat`, `pithos.pyw`, and the `pithos` folder), the quickest way to "paste the code over the executable" is:

1. Download the latest ZIP from the Releases page and extract it to a temporary folder such as `Downloads\pithos-latest`.
2. Open the extracted folder. You should see subfolders like `pithos` and `data` plus the launcher scripts (`pithos.bat`, `pithos.pyw`).
3. Select everything **except** `Pithos.exe` and `uninstall.exe` (those come from the original installer) and copy it.
4. Paste the files into your existing installation directory (the one that already contains `Pithos.exe`). When Windows prompts you, choose **Replace the files in the destination** so the updated Python sources inside `pithos\pandora`, `pithos\plugins`, `pithos\*.py`, and the `data\ui` dialogs overwrite the old ones.
5. Launch `Pithos.exe` or `pithos.bat` as usual. The next run will pick up the refreshed code, so the dark theme toggle and other updates immediately become available without reinstalling anything else.

These steps are safe because the `.py` and `.pyw` files are what drive the application logic. `Pithos.exe` is just a small bootstrapper that delegates to those scripts, so replacing the scripts leaves the executable intact.

Notes
-----

You must remove pygtk if installed with an older version.

If Python is installed to a custom directory(not C:\python27) it must be in the PATH environment variable to work (google to find out how)

If previous versions crashed please try out the newest version as this has been resolved.

Dark theme
----------

Pithos now ships with an optional dark GTK theme that can be toggled at runtime:

1. Launch Pithos and choose **Edit → Preferences** (or press <kbd>Ctrl</kbd>+<kbd>P</kbd>).
2. In the **General** tab, tick **Enable built-in dark theme**.
3. Close the dialog — the darker palette is applied immediately and the preference is saved to your existing `pithos.ini` so it persists the next time you start the app.

If you ever want to go back to the default look, simply return to the same checkbox and clear it.

------------------

![Pithos for Windows Screenshot](http://i.imgur.com/PcAMD.png)

------------------

Pithos is not affiliated with or endorsed by Pandora Media, Inc.
