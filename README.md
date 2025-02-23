# Tapo P110M toggle

Very simple script to toggle TP-Link P110M smart plugs on and off.

Built to use with Elgato Stream Deck.

Requires [tapo](https://github.com/mihai-dinculescu/tapo) module.


## Usage

- Install with `poetry install`
- Activate your poetry virtualenv (I set `poetry config virtualenvs.in-project true` to keep this simple)
- Set the following envvars:
  - `TAPO_USERNAME`  - your TP-Link username
  - `TAPO_PASSWORD` - your TP-Link password
  - `TAPO_P110M_IP_ADDRESS` - IP address of your smart plug
- The username/pass are the same you'd use to log in to the Tapo app or TP-Link website. The IP address is usually an IP for a device on your local network.


With all that in place, you can simply call the script with to toggle your switch on an off - for example, with `python3 p110-toggle.py`.