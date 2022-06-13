<div align="center">
  <a href="https://github.com/fledpaul/cenera">
    <img src="img/Alis.png" height="150" width="375">
  </a>
    <h3 align="center">ALIS - Automatic Library Installation Software</h3>
  <p align="center">
    ALIS can be easily integrated into your project and the required libraries are installed directly at the first start or
    updates.
    <br/>
    <a href="https://fled.dev/alis"><strong>View Details»</strong></a>
    <br/>
    <br/>
    <a href="mailto:report@fled.dev">Report Bug</a>
    ·
    <a href="mailto:request@fled.dev">Request Feature</a>
  </p>
</div>

## About The Project
<br>
With ALIS all libraries are installed directly at the first start of your program.

### Built With
* [Python](https://python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/)

## Usage
  Unzip the zip file & open the `config.json´
  ```sh
  cd /alis-main/
  ```
In it you will now see several variables. The variable `updated` should be set to `false` by default. In the variable `libs` you can now enter all libraries that should be installed, separated by a space. In the variable `success_msg` you can enter a message, which should be output on a successful installation. Finally you write in the `run_py` variable only the file path/your file name.

Now you just have to drag the `alis.py` and `alis.json` into your program folder and you are done! The user now has to execute the `alis.py` at every start. You should note this in your readme file. Of course you can rename the file or modify it in some other way.
  
 ## Roadmap
- [ ] Add .exe
- [ ] Add .appimage
- [ ] Add .log
- [ ] Multi-Language Support
    - [ ] German
    - [ ] Spanish
    - [ ] Mandarin
    - [ ] Hindi
    - [ ] French

## Donations
```sh
Bitcoin: bc1q0jlnpzyewqxn4dlmn5kxplq0etchhjf880mw64
```

```sh 
Bitcoin Cash: qp9fxxrejkwp0zmrd3kjavd7xt7c7gdx0uar7f9j6w
```

```sh
Ethereum: 0x0B58C4FA54E81193E60dc0312f98C3738999fC45
```

```sh
Zilliqa: zil1m6eyqm7flq2cwkxm8l60g836a75yq5mtdzlcjw
```

Each donation will be distributed among contributors.

## License
Distributed under the GNU License. See `LICENSE.txt` for more information.
