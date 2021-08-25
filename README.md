resizePixel
==========================

[![Build Status](https://travis-ci.org/mtchavez/python-package-boilerplate.png?branch=master)](https://travis-ci.org/mtchavez/python-package-boilerplate)
[![Requires.io](https://requires.io/github/mtchavez/python-package-boilerplate/requirements.svg?branch=master)](https://requires.io/github/mtchavez/python-package-boilerplate/requirements?branch=master)

change quality of the image

## Package

Basic structure of package is

```
├── README.md
├── resizePixel
│   ├── __init__.py
│   ├── resizePixel.py
│   └── version.py
├── pytest.ini
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── helpers
    │   ├── __init__.py
    │   └── my_helper.py
    ├── tests_helper.py
    └── unit
        ├── __init__.py
        ├── test_example.py
        └── test_version.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

    Start the tests


## Usage

<code>

    # import library

    from resizePixel.resizePixel import rpImage,reduce_qualtiy
    from PIL import Image

    # image path
    image_path = "img.jpg"

    # open the image and check the current quality
    image_file = Image.open(image_path)
    my_image = rpImage(image_path,image_file)
    info = my_image.get_image_meta()
    print(info)

    # decrease quality explained above
    new_image = reduce_qualtiy(image_path,image_file,quality=50)
    print(new_image)
        
</code>
