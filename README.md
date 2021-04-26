# img-to-ascii
A Python script that converts images to ascii characters.

## Context
Just a quick script I made for fun. It's fairly simple - convert the RGB values to greyscale, then use the greyscale value to pick from a list of predefined ascii characters.

## How to Use
Run the following command with the image file you would like to convert:

```
$ python to_ascii.py <IMG-FILE>
```

It will ask you for an interval size - this represents the width of the square of pixels per ascii character.

The ascii version will be stored in the `output.txt` file.

## Preview

**Before**

![Before](https://raw.githubusercontent.com/defCoding/img-to-ascii/master/image.png)

**After**

![After](https://i.imgur.com/IK3YpwK.png)
