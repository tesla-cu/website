
# TESLa - Turbulence Energy Systems Laboratory at the University of Colorado

Welcome to the source code based on the [Hugo](https://gohugo.io) [Academic](https://sourcethemes.com/academic/) theme that builds the [TESLa website](teslacu.org). The purpose of this `README.md` is to briefly describe how to add new content and modify the website. We assume some prior knowledge of how [github works](https://www.atlassian.com/git/tutorials/syncing/git-push) and basic terminal usage. See [Academic](https://sourcethemes.com/academic/) for a thorough description of all functionality.

# Adding New Content

New to the lab? Just published an article? Congratulations! You probably want to show off to all your friends right? You came to the right place.

Note, if you already have a fork, be sure to follow instructions under "Conflicts" _first_. You want to be working from up to date code before commiting new code so conflicts do not arise.

## Configuring your github account

We follow the convention of forking the repository, modifying your source code, then submitting a pull request where other members of the lab can inspect you new content. Note that there are probably an infinite number of ways of doing the same thing, we just describe one way.

At the [website source code](https://github.com/tesla-cu/website), click "Fork" in the top right and create a repository in your personal github account. Now go to your personal github page and clock "Clone or download." Copy that link. Open a terminal up (assuming unix based system) and go a folder where you would like to place the source code. Execute `git clone [URL]`. You should now see the folder containing the website source code. One last critical step is to follow [these directions](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork) to configure a remote to point at the website hosted by [tesla-cu](https://github.com/tesla-cu/website). This will allow you to get stay up-to-update with the upstream repository.

## Building the website locally

[Hugo](https://gohugo.io) provides functionality to build the website locally and very simply. Follow the instructions [here](https://gohugo.io/getting-started/installing/#quick-install). Once you have hugo installed, open a terminal in the website directory and execute `hugo server`. There are a bunch of optional arguments you can choose to add after `server` (i.e., `-D`) to test various things, but are not necessary. In a web browser, go to http://localhost:1313/ . You should now see the website built from the local source code! As you add and edit files, save the files and the website will update automatically. 

## Actually adding the content

You are now set to add new content. Go under `content/` and start adding! The key thing that you should be aware of is that much of the source code is based on patterns, so don't go deviating from the norm. Here are a brief set of instructions on how to add a few key items:
- **People:** go to `content/authors/`, copy a folder of a person (`cp -r old_author new_author` should do the trick), change the new folder name and modify the content inside the new folder
- **TESLa Publications:** go to `content/publication/`, copy a folder of a publication , change the new folder name and modify the content inside the new folder
- **Personal Publications:** these would be publications that you did without any affiliation at all with TESLa. Create a `.md` file in your personal author folder and format it similarly to a publication `index.md` file except with a different name. See `content/authors/michael_meehan/` for an example.

A more complete set of convensions **you should follow** are in the files:
- FILE
- FILE

Feel free to use these as a basis as well.

## Merging new information

Now that you have added all the content you wanted, it's time to get onto the website! 

### Add and commit
First, execute
- `git add file`
- `git commit -m "message"`

Please, **do not use `add *` or `add .`**. Be cognizant of what you are adding. There can be strange files that appears and conflicts with building the website. We also recommended breaking down the commits to be specific (i.e., "added buoyant jet publication" not "added stuff"). If you are adding a lot, add files in groups and commit each group with your specific message.

### Conflicts
Next, we need to check that you don't conflict with your fork or the tesla-cu repo. You can/should do this before adding new code (as stated above) so conflicts _do not_ arise. Execute
- `git fetch`
- `git pull`
- `git fetch upstream`
- `git pull upstream`

If you don't have any conflicts, you are good to go! If you do, you will need to [resolve them](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line). 

### Push and pull
Finally, execute `git push` from your the website directory. This will update the code on your personal repository. Go online to your github profile. Under your fork, click the "Pull Request" tab then "New Pull Request." Review all the updates, provide a clear message, and submit the PR. Another contributor will take a look at your code to make sure it is good to go before merging into the master branch.

### Review process
If the reviewer(s) of the code want(s) a modification (i.e., missing data, typos, etc.), simply repeat the above processes. Once you finally push an updated version of the code to your personal fork, this will update the PR, and the reviewer(s) can see the modifications you have made. This can be repeated until the reviewer(s) is satisfied.

# Modifying the Website Format

So you want to be a website developer eh? You came to the right place. We will outline some of the basic information you need to make structural changes to the website pages.

## Editing the homepage

The homepage is comprised of menus found at `config/_default/menus.toml` and widgets at `content/home/`. In `menus.toml`, a trailing `/` in the `url = ` field creates a new page for it while a leading `#` links the widget in `content/home/` with the same name, so clicking that menu option just scrolls you down to where that widget is located on the homepage. If a `/` is used, the `_index.md` file in the corresponding directory is guide to designing that page.

The widgets in `content/home/` are simply the markdown files located in the folder. You can simply add new widgets by creating a new markdown file in that folder and making it visible (a setting in the `.md` file). There are a bunch examples there already that are not visible and all of the widgets to choose from can be found in `layouts/partials/widgets/` with the corresponding `.html` file extension. Note that the `content/people/` directory created a new widget page to filter groups of people simply by adding a `index.md` file to the folder.

## Modifying source code

Modifying the source code is a good way to adjust and manipulate pages slightly. We did this with the author homepages to include personal publications. This code is found in `layouts/` and the corresponding folder name. To be honest, you are just going to need to play with the codes from here to really understand how they work (i.e., delete some things and see how the website is updated). 

# Tips and Tricks

A number of times I have broken the website where it won't compile. I then perform a standard Ctrl + z to get back to the original code before it broke, and localhost still shows an error. **Don't panic.** Open `config/_default/config.toml` and resave that file and you should be good to go. There is probably an option in `hugo server` to avoid this but I haven't cared enough to investigate. - MAM


# License

Copyright 2016-present [George Cushen](https://georgecushen.com).

Released under the [MIT](https://github.com/gcushen/hugo-academic/blob/master/LICENSE.md) license.

[![Analytics](https://ga-beacon.appspot.com/UA-78646709-2/hugo-academic/readme?pixel)](https://github.com/igrigorik/ga-beacon)
