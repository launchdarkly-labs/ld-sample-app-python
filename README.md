# LaunchDarkly Sample App for Python and JavaScript

## Requirements

* Python 3.12 or higher
* LaunchDarkly Flags:
  - **Release: UI Enhancements**, key: `release-ui-enhancements`
  - **Release: Home Page Slider**, key: `release-home-page-slider`
  - **Coffee Promo 1**, key: `coffee-promo-1`
  - **Coffee Promo 2**, key: `coffee-promo-2`
  - **Banner Text**, key: `banner-text`

## Setup

To get started, clone this repo locally

```
git clone https://github.com/launchdarkly-labs/ld-sample-app-python.git
cd ld-sample-app-python
```

Create a virtual environment

```
python -m venv ldsampleapp
```

Activate the environment

```
source ldsampleapp/bin/activate
```

Install libraries

```
pip install -r requirements.txt
```

Add LaunchDarkly keys

* Rename `.env.example` to `.env`
* In the `.env` file, replace the fake keys with your LaunchDarkly SDK key and client-side key

## Run

To run the site:

```
python app.py
```

In your browser, navigate to:

```
http://localhost:3000
```

When you're finished and wish to exit the virtual environment:

```
deactivate
```

Enjoy!