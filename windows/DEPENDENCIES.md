# Large installer dependencies

These runtime installers are intentionally **not** stored in this repository because they are large third-party binaries. The NSIS installer can download them automatically, or you can download them manually and keep them outside git.

| Dependency | Expected filename | Size | URL used by `install.nsi` |
| --- | --- | ---: | --- |
| Python 2.7.3 | `python-2.7.3.msi` | 15 MB | `http://python.org/ftp/python/2.7.3/python-2.7.3.msi` |
| GStreamer.com SDK 2012.9 | `gstreamer-sdk-x86-2012.9.msi` | 97 MB | `http://www.freedesktop.org/software/gstreamer-sdk/data/packages/windows/x86/gstreamer-sdk-x86-2012.9.msi` |

## Manual/offline build flow

If you do not want the installer to download these files at install time:

1. Download the two files above manually.
2. Put them in the `windows` folder next to `install.nsi` before building/running the installer.
3. Keep the filenames exactly as listed in the table.
4. Do **not** commit them; `.gitignore` excludes `*.msi` and `*.exe`.

The existing NSIS download helper checks for a local file with the expected filename before downloading. If it finds one, the installer prompts to use that local copy.
