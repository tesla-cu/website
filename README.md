# Turbulence Energy Systems Laboratory (TESLa) Website

Welcome to the source code of the  [TESLa website](https://teslacu.org) powered by the [Hugo](https://gohugo.io) [Academic](https://sourcethemes.com/academic/).

## Quickstart
Running this website locally requires `hugo` to be [installed](https://gohugo.io/getting-started/installing/#quick-install) on your machine. The website requires a minimum version so we recommend
```
brew install hugo
```
on macOS or
```
wget https://github.com/gohugoio/hugo/releases/download/v0.58.2/hugo_0.58.2_Linux-64bit.deb
dpkg -i hugo_0.58.2_Linux-64bit.deb
```
on Ubuntu since standard `sudo apt-get` installs a depreciated version.

Once `git` and `hugo` are installed, create a fork from [our repository](https://github.com/tesla-cu/website). This will create an exact copy under your username. Then perform: 
```bash
$ git clone --recursive https://github.com/[username]/website.git
$ cd website
$ hugo server
```
where you should replace `[username]` with your username. Open [http://localhost:1313/](http://localhost:1313/) and your personal build of the website should appear. Once you are satisfied with your updates, submit a pull request where other members of the lab can inspect and merge your new content. Check [Configuring your Github account](https://github.com/tesla-cu/website/wiki/Configuring-your-Github-account) wiki page to help you with this procedure.

If you would like to add a new content additional enrichment or help to improve the website design, check out our [Adding new content](https://github.com/tesla-cu/website/wiki/Adding-new-content) and [Modifying the website format](https://github.com/tesla-cu/website/wiki/odifying-the-website-format) pages on the wiki! See [Hugo Academic docs](https://sourcethemes.com/academic/docs/) for a thorough description of all functionality.

## Quick File Location Reference
Personal information and profile pictures are located under
```
content/authors/firstname_lastname
```
You can upload your CV to
```
static/files/authors_cv/firstname_lastname_cv.pdf
```
and can add it to `_index.md` under your personal information as
```
- icon: cv
  icon_pack: ai
  link: files/authors_cv/firstname_lastname_cv.pdf
```

## Formatting/Content Tips
There have been cases where people have used webscraping bots to pull phone numbers from our CVs posted on this website - it's recommended to omit that information from the PDF that you upload here.