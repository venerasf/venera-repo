# Venera Repository

This repository contains the scripts to be used with [venera](https://github.com/farinap5/Venera).

Take a look at [venera.farinap5.com/6-venera-package-manager.html](https://venera.farinap5.com/6-venera-package-manager.html).

Wanna upload a new script? Please, create a **issue** informing about your code.

---

## Customized Repository

This guide will help you set up and use a customized repository for organizing and compiling your code into packages used by VPM (Venera Package Manager).

Create the repository with the codes organized my folders. To compile your package with references to download the scripts, run the `main.py` script.

Before running main.py, you need to configure your repository URL, name, and email. Open main.py and locate the following configuration block:

```python
    repo_conf = Repo(
        Root: ".",
        Name: "farinap5 <email>",
        Version: 1.0,
        Description: "Default Package From Venera",
        URL: "http://r.venera.farinap5.com")
```

Update the `repo_conf` parameters, replace the URL to the endpoint where VPM will look for the data. Set your name, email as well.

To create a signature for your generated package, use `vpm-signer` (https://github.com/venerasf/vpm-signer). For more detailed instructions and information, please refer to the full documentation provided in the repository.