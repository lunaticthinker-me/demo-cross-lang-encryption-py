# Encrypt/Decrypt Example

Encrypt/Decrypt Example for the Set of Articles [Cross Programming Language Encryption *](https://lunaticthinker.me/index.php/cross-programming-language-encryption-csharp-part-1/).

[![Python Version](https://img.shields.io/badge/Python-3.6%7C3.7%7C3.7%7Cdev-blue)](https://img.shields.io/badge/Python-3.6%7C3.7%7C3.7%7Cdev-blue)
[![TravisCI](https://travis-ci.org/lunaticthinker-me/demo-cross-lang-encryption-py.svg?branch=master)](https://travis-ci.org/lunaticthinker-me/demo-cross-lang-encryption-py)
[![Contributions welcome](https://img.shields.io/github/contributors/lunaticthinker-me/demo-cross-lang-encryption-py)](https://img.shields.io/github/contributors/lunaticthinker-me/demo-cross-lang-encryption-py)

[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=lunaticthinker-me_demo-cross-lang-encryption-py&metric=alert_status)](https://sonarcloud.io/dashboard?id=lunaticthinker-me_demo-cross-lang-encryption-py)
[![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=lunaticthinker-me_demo-cross-lang-encryption-py&metric=coverage)](https://sonarcloud.io/component_measures/metric/coverage/list?id=lunaticthinker-me_demo-cross-lang-encryption-py)
[![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=lunaticthinker-me_demo-cross-lang-encryption-py&metric=bugs)](https://sonarcloud.io/component_measures/metric/reliability_rating/list?id=lunaticthinker-me_demo-cross-lang-encryption-py)
[![SonarCloud Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=lunaticthinker-me_demo-cross-lang-encryption-py&metric=vulnerabilities)](https://sonarcloud.io/component_measures/metric/security_rating/list?id=lunaticthinker-me_demo-cross-lang-encryption-py)


[![Donate to this project using Patreon](https://img.shields.io/badge/patreon-donate-yellow.svg)](https://patreon.com/dragoscirjan)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QBP6DEBJDEMV2&source=url)

<!--[![Donate to this project using Flattr](https://img.shields.io/badge/flattr-donate-yellow.svg)](https://flattr.com/profile/balupton)
[![Donate to this project using Liberapay](https://img.shields.io/badge/liberapay-donate-yellow.svg)](https://liberapay.com/dragoscirjan)
[![Donate to this project using Thanks App](https://img.shields.io/badge/thanksapp-donate-yellow.svg)](https://givethanks.app/donate/npm/badges)
[![Donate to this project using Boost Lab](https://img.shields.io/badge/boostlab-donate-yellow.svg)](https://boost-lab.app/dragoscirjan/badges)
[![Donate to this project using Buy Me A Coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg)](https://buymeacoffee.com/balupton)
[![Donate to this project using Open Collective](https://img.shields.io/badge/open%20collective-donate-yellow.svg)](https://opencollective.com/dragoscirjan)
[![Donate to this project using Cryptocurrency](https://img.shields.io/badge/crypto-donate-yellow.svg)](https://dragoscirjan.me/crypto)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://dragoscirjan.me/paypal)
[![Buy an item on our wishlist for us](https://img.shields.io/badge/wishlist-donate-yellow.svg)](https://dragoscirjan.me/wishlist)
-->

- [Encrypt/Decrypt Example](#encryptdecrypt-example)
  - [Compatibility](#compatibility)
  - [Getting Started](#getting-started)
    - [Prereqiusites / Dependencies](#prereqiusites--dependencies)
    - [Installation](#installation)
    - [Development](#development)
      - [Requirements](#requirements)
        - [For Windows](#for-windows)
        - [For Linux/Unix/OSX](#for-linuxunixosx)
    - [Testing](#testing)
    - [Running](#running)
  - [Authors](#authors)
  - [Issues / Support](#issues--support)

<!-- /TOC -->

## Compatibility

| Language/Algorithm | C# | Go | Js | Py |
| AES/CFB | ? | ✓ | ✓ | ✕ |
| AES/CFB | ✓ | ✕ | ✓ | ✓ |
| AES/CBC | ✓ | ✓ | ✓ | ✓ |
| RSA/OAEP |  |  |  |  |
| RSA/PCKS1V15 |  |  |  |  |

#### Known Issues / Troubleshooting

- On Windows, you will need to install `M2Crypto` manualy: 
```powershell
pip install https://ci.appveyor.com/api/buildjobs/jw1kqpwsbur77mxi/artifacts/dist/M2Crypto-0.35.2-cp38-cp38-win_amd64.whl
```

### Installation

```bash
git clone https://github.com/lunaticthinker-me/demo-cross-lang-encryption-py
```

### Development

#### Requirements

- Please install [Python](https://python.org). Project support **python 3.6 and above**.
- Please instal a Python IDE
  - [Visual Studio Code](https://code.visualstudio.com/) with [ITMCDev Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=itmcdev.python-extension-pack)
  - [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
  - [Vim](https://www.vim.org/) (see here a [tutorial](https://www.fullstackpython.com/vim.html) for making Vim a Python IDE)
  - Any other IDE you trust.

##### For Windows

- Please install [git-scm](https://git-scm.com/download/win) tool.
- Please install a form of make/cmake
  - Install [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm)
  - Install [make](https://sourceforge.net/projects/ezwinports/files/) from [ezwinports](https://sourceforge.net/projects/ezwinports/files/)
  - Install [chocolatey](https://chocolatey.org/), run `choco install make`
  <!-- - Install [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)
    - You will find it under `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.25.28610\bin\Hostx64` -->

##### For Linux/Unix/OSX

- Please install `git` and `make`

```bash
sudo apt-get install git make -y
```

### Testing

Run unit tests using `make test`.

### Running

Please run `make run`

Demo output:

```
// AES Encrypted Values:
PY_AES_CFB8_128 = 'PtjaRlGwX8Gx5t/DU5ZeCG0ORrB1rJa/VJ2tUthtCaM='
PY_AES_CFB8_192 = 'g/5yb1eOSiiQHS0B5xNmhuzJ2YhbRcA7inB/t+gpOwE='
PY_AES_CFB8_256 = 'miNCtb9/yRPRxZESeW58REdLNylTnVcP+hhAdqKemNs='
PY_AES_CBC_128 = '3kRpT6B91EnC+ewGHWW0VnnLRn4ADPSb1GjSIf2fvyAmJ/cU8/bEZsdzOxvusC6f'
PY_AES_CBC_192 = '+JLRXRGqCQgH3tfKrHmnW923jYmYVpvOhVTWUocuYKf3puj5nSl60ZuDveVNQG60'
PY_AES_CBC_256 = 'UmaD3yNPhnh4cFg7mRBcRD224QMIFZcwcl7NdC0biMoGZPoUmzAZLsZ0UuRwRcgN'
// RSA Encrypted Values:
PY_RSA_PKCS1V1_5 = 'NCqEhkZwZYplXt2IjAwEd2BhPmfSu20JypRtE3jGtzarP+WyaUuuE412ZbE/NA5kBSZb79x66i6qoWmZFpLjIdK7efOAvXhrPEFYn5cC6bS1SWsX+JrltzYeQjMnHiCC7vjrDGDEQ5HYemMZVBvNihqG/HnkAsyWmKrANro7CxtvXaPLBIoIscX2+uolVz7v4Q0KWztnRmghmCiluUxgH0RNA3bLiCPJTzXt9rNMZZ+8tfgYro+a6ciq8Qex3r4NgJyQHDcNBZ28hQaBEyURCVDkxpTvDXrGQMBswf4KbGH02E4Uw55MZ6ioaSZf1YW8CFioRImM9UOltWb+dsXh+A=='
PY_RSA_OAEP = 'ORn151YT9bB7HnNgDfwulIhJEX+WDv47CqZQ5RVeNs2UvyQ7uBsh6Kjg+P2AFF0NxJxqwGDuExG/vkwnXUr8JgSQWibHuNTdm477q6lO+BD6uVQPwhEpfoSt+n7nmHZvGPMhMdtGlxb/aa5jErfwnwqSDQiFwqzoDAz7FX+QDBspjr5zI6KCcrkmApAXq93lDIvFozRve6iQpJyRTML/ph206hvzwUF/ZpshtpHnqFDfd/4hoO9AEx3NKOQmlKE8Cce3V/VgcgUILhzTtT8t180NPcbLfAnom8zOrrGH8iD4ODBi2qg5dZesQpIWw/1fMxrWRlWtniErNgHR0Nw6/A=='
// X509 Encrypted Values:
PY_X509 = 'WCggI2zW1gn6tXAKhBbFPebFNj1s0t/sW8yg3Ieg3HkOsLifAyF5gg8fclilqqMjl6+6VnJPhEDE+n5MFgvdeFCUqNBBNSiG7YiQwDgEzVx5C2hWQwictwImV83gKt/HokS3j0xM9TCPGzOiFUvZgoZJd3EOa73wWTOLtgvMfNWY0Z/D8LBhEI3gbVtznPDIRwUV4ad0on/ilsqnSuUUyH1G4mGDcf4BoklVyMCoGEmu5msUMedECjLpeKehZKhcPwDq8t88oq18f0hvQt2eF15vWoa78LZk7lHTz+k0h2zbAFupEHaHIfv/KpnokHSsFDLiNycV6GEzXYShg6nL8Q=='
```

## Authors

- [Dragos Cirjan](mailto:dragos.cirjan@gmail.com) - Initial work - [Encrypt/Decrypt Example](/lunaticthinker-me/demo-cross-lang-encryption-py)

See also the list of contributors who participated in this project.

## Issues / Support

Add a set of links to the [issues](/lunaticthinker-me/demo-cross-lang-encryption-py/issues) page/website, so people can know where to add issues/bugs or ask for support.

<!-- ## Changelog

Small changelog history. The rest should be added to [CHANGELOG.md](CHANGELOG.md).

See here a template for changelogs: https://keepachangelog.com/en/1.0.0/

Also see this tool for automatically generating them: https://www.npmjs.com/package/changelog -->
