# Tiniest Static Website Generator
This is a very simple application to compile Markdown files into HTML


## What is `tiniest`?  
`tiniest` is a Static Website Generator, which reads Markdown files and generates HTML files for each Markdown. It scans the directory it has been executed from recursively and search for Markdown files. 

## Why I created `tiniest`?  
I used [Hugo](https://gohugo.io/) earlier to create a couple websites. It's a good and capable system, I am grateful to its creators. Unfortunately for the archive website I want to build it is too capable and too complex. I don't want to manage archetypes, themes, layouts etc.

Also my WSL environment caused some issues during the Hugo update which I was too lazy to fix.

So I decided to create a new Static Website Generator which is only capable of creating HTML files from Markdown files. This decision also a result of my laziness, I didn't want to write HTML by hand, but I can write Markdown.

That's how and why `tiniest` was born.

## How to use `tiniest`?  
### Installation and Requirements  
`tiniest` depends on one non-native Python package, which is [Python-Markdown](https://python-markdown.github.io/)

You can install this package via `pip install markdown`

Then to install `tiniest` you can clone the git repository via `git clone git@github.com:CanburakTumer/tiniest_static_website.git`

### Running the app
From the directory where your source Markdown files are located, call the following command `python <PATH_TO_TINIEST_REPO>/src/tiniest.py [FLAGS]`

After that `tiniest` will scan the working directory for Markdown files to process, and it will log the processed file list to the stdout unless there is an error. If there is an error it will also log the error to the stdout.

#### Flags
- `-d` or `--debug`: When debug flag is provided, the application becomes more verbose and logs steps into the stdout.   


### Adding metadata to your Markdown files
`tiniest` builds the HTML body from the information in the Markdown files. But of course a web page might also need some header information like title. To enable this in the `tiniest` I created a metadata system.

- Metadata part must be in the beginning of the Markdown file
- There must be only one metadata section in the Markdown file
- Metadata section must start with `<<<tiny` and end with `tiny>>>`
- Every label should be on its own line followed with a new-line character

Currently (as of v2023.12.29) there are two labels `tiniest` can process and add to head section of the HTML.

#### Title
`title:` is the keyword for the label, page title should be written between the keyword and the new-line character

#### Style
`tiniest` can include css files into the head section of the generated HTML as the external file. `style:` keyword should be used to define css file's path. And the path should be followed by a new-line character.

#### Custom
`tiniest` can now include your custom code in the `head` section of HTML. `custom:` keyword followed by path to the code. It MUST be followed by a new-line character. I implemented this to add GA4 tracking into my blog. But it can be used to add custom JavaScript or CSS to bring your pages to life.

### About `.tiny` file
This file currently (as of v2023.12.29) only stores the last run date of the `tiniest`. To be cost effective when `tiniest` runs it only processes the modified Markdown files. To find the correct files, `tiniest` depends on the information in the `.tiny` file.

~~Until the `--all` flag added, you can achieve the same result with deleting the `.tiny` file.~~ Added with v2024.01.14  

## Sample Website and Repository  
I started creating my own [blog archive](http://archive.canburaktumer.com) using `tiniest` also I may move my [build-in-public](http://build.canburaktumer.com) blog from [Hugo](https://gohugo.io/) to `tiniest`.  

You can see the Markdown files and the HTML files for my archive in the [GitHub](https://github.com/CanburakTumer/archive_website) repository.

## Some practices you may follow  
You can add following line to the `.gitignore` file
```
.tiny
*.md
```

These two lines will block `.tiny` file and Markdown source files to be pushed to the git repository. So the repository will only store the website documents. _Although I pushed my Markdown sources as well to my archive repository to also archive those._

## Contribute
- If you hit a bug feel free to create an [issue](https://github.com/CanburakTumer/tiniest_static_website/issues/new)  
- If you think there is a missing feature, again feel free to create an [issue](https://github.com/CanburakTumer/tiniest_static_website/issues/new)  
- If you want to fix a bug or develop a feature yourself, fork the repo and send the PR  
- If `tiniest` helped you and you want to help my costs you can become a [sponsor](https://github.com/sponsors/CanburakTumer)  

## Roadmap  

See [CHANGELOG](CHANGELOG.md) for details.

- Re-choose the license.
- ~~Add a new flag to regenerate HTML files from **all** Markdowns~~ Added with v2024.01.14  
- ~~Add a new flag to execute a dry run to see which files will be processed~~ Added with v2024.01.14
- Turn this into a PyPi package to be called from terminal

## Thanks
I would like to thank to [ehaspulat]() for being so kind to comment on the first working version of this code. His comments also encouraged me to continue.