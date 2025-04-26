 
#  Writing your first community tutorial 
Stay organized with collections  Save and categorize content based on your preferences. 
This space is dedicated to Earth Engine users who want to share their knowledge with the rest of the Earth Engine community. Created by Earth Engine users, for Earth Engine users, tutorials in this section are intended for all levels, from beginner to more advanced users.
Tutorials may be submitted as plain text and code formatted using the Markdown markup language, or as Colab notebooks containing Markdown and executable Python code. Tutorials built using the Earth Engine JavaScript client libraries are generally written in Markdown, while Colab is recommended for tutorials based on the Earth Engine Python client libraries.
## Before you begin
### Code of Conduct
The Earth Engine team is committed to fostering a harassment-free and inclusive community. Please familiarize yourself with our [Code of Conduct](https://opensource.google/docs/releasing/template/CODE_OF_CONDUCT/) before contributing.
### Joining GitHub
Earth Engine community tutorials are shared and reviewed through GitHub. If you don't already have a GitHub account, you must first create one at https://github.com/join.
### Proposing a tutorial
Before investing significant time and effort on a new tutorial, potential contributors are asked to submit a simple proposal with some basic information. This allows authors to work with the maintainers of the Earth Engine developer documentation to focus efforts on tutorials that provide the most value to the Earth Engine user community. It also saves time by avoiding potential back-and- forth during the review process.
[Propose a tutorial](https://github.com/google/earthengine-community/issues/new?assignees=gino-m%2C+tylere&labels=tutorial+proposal&template=propose-a-tutorial.md&title=%5BTutorial+proposal%5D+Your+tutorial+title+here)
### First time setup
If this is the first time you're submitting a tutorial to the Earth Engine community GitHub repository, be sure to complete these steps _before_ starting work on your tutorial:
  1. Accept the Contributor License Agreement (CLA) at:
https://cla.developers.google.com
  2. Read and internalize the [Community Tutorial Style Guide](https://developers.google.com/earth-engine/tutorials/community/styleguide).


## Writing and submitting a tutorial
Once your tutorial proposal is accepted by the maintainers, there several options for editing the tutorial and for submitting it to the Earth Engine community repository:
### Markdown quick start
You can fork the GitHub repository and create a new tutorial directly via the GitHub website to quickly get started without additional tools or setup:
  1. If you haven't already, [sign into GitHub](https://github.com/login).
  2. To create and edit a new tutorial file, click _New tutorial_. You'll be prompted to fork the repository, if needed.
[New tutorial](https://github.com/google/earthengine-community/new/master/tutorials?value=---%0Atitle%3A%20Your%20tutorial%20title%0Adescription%3A%20A%20short%20description%20of%20the%20tutorial%2C%20all%20on%20one%20line%20with%20no%20carriage%20returns.%0Aauthor%3A%20your-github-username%0Atags%3A%20comma-separated%2C%20lowercase%2C%20list%2C%20of%2C%20related%2C%20keywords%0Adate_published%3A%20YYYY-MM-DD%0A---%0A%3C%21--%0ACopyright%202023%20The%20Google%20Earth%20Engine%20Community%20Authors%0A%0ALicensed%20under%20the%20Apache%20License%2C%20Version%202.0%20%28the%20%22License%22%29%3B%0Ayou%20may%20not%20use%20this%20file%20except%20in%20compliance%20with%20the%20License.%0AYou%20may%20obtain%20a%20copy%20of%20the%20License%20at%0A%0A%20%20%20%20https%3A//www.apache.org/licenses/LICENSE-2.0%0A%0AUnless%20required%20by%20applicable%20law%20or%20agreed%20to%20in%20writing%2C%20software%0Adistributed%20under%20the%20License%20is%20distributed%20on%20an%20%22AS%20IS%22%20BASIS%2C%0AWITHOUT%20WARRANTIES%20OR%20CONDITIONS%20OF%20ANY%20KIND%2C%20either%20express%20or%20implied.%0ASee%20the%20License%20for%20the%20specific%20language%20governing%20permissions%20and%0Alimitations%20under%20the%20License.%0A--%3E%0A%0AIn%20a%20few%20sentences%2C%20describe%20what%20the%20user%20is%20going%20to%20learn.%20Be%20sure%20to%20include%0A_concise_%20background%20information%3B%20only%20include%20what%27s%20helpful%20and%20relevant.%0AWhen%20in%20doubt%2C%20leave%20it%20out%21%0A%0A%23%23%20Section%20heading%201%0A%0ABreak%20up%20your%20tutorial%20into%20manageable%20sections.%0A%0AWith%20one%20or%20more%20paragraphs%2C%20separated%20by%20a%20blank%20line.%0A%0AInside%20your%20sections%2C%20you%20can%20also%3A%0A%0A1.%20Use%20numbered%20lists%0A1.%20..when%20the%20order..%0A1.%20..of%20items%20is%20important.%0A%0AAnd%3A%0A%0A-%20This%20is%20a%20bulleted%20list.%0A-%20Use%20bulleted%20lists%20when%20items%20are%20not%20strictly%20ordered.%0A%0A..and%20even%3A%0A%0AUse%20%20%20%20%20%7C%20tables%20%20%20%7C%20to%20organize%20%7C%20content%0A-------%20%7C%20--------%20%7C%20-----------%20%7C%20-------%0AYour%20%20%20%20%7C%20tables%20%20%20%7C%20can%20%20%20%20%20%20%20%20%20%7C%20also%0Acontain%20%7C%20multiple%20%7C%20rows%20%20%20%20%20%20%20%20%7C%20...%0A%0A%23%23%20Section%20heading%202%0A%0AUse%20separate%20sections%20for%20related%2C%20but%20discrete%2C%20groups%20of%20steps.%0A%0AUse%20code%20blocks%20to%20show%20users%20how%20to%20do%20something%20after%20describing%20it%3A%0A%0A%60%60%60js%0A//%20Use%20comments%20to%20describe%20details%20that%20can%27t%20be%20easily%20expressed%20in%20code.%0A//%20Always%20try%20making%20code%20more%20self%20descriptive%20before%20adding%20a%20comment.%0A//%20Similarly%2C%20avoid%20repeating%20verbatim%20what%27s%20already%20said%20in%20code%0A//%20%28e.g.%2C%20%22assign%20ImageCollection%20to%20variable%20%27coll%27%22%29.%0Avar%20coll%20%3D%20ee.ImageCollection%28%27LANDSAT/LC08/C02/T1_TOA%27%29%3B%0A%60%60%60%0A%0A%23%23%23%20Use%20subsections%20if%20appropriate%0A%0AConsider%20breaking%20longer%20sections%20that%20cover%20multiple%20topics%20or%20span%20multiple%0Apages%20into%20subsections.)
  3. Enter a name for the tutorial file of the form:
`your-tutorial-name/index.md`
Where `your-tutorial-name` is the short name of your tutorial in all lowercase. Use dashes ("-") to separate words. Do not use spaces or any other punctuation in the folder name.
  4. Edit your tutorial directly in the GitHub file editor, using "Preview" to verify the formatted output (see also [Editing files in your repository](https://help.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository) in the GitHub documentation).
  5. Once ready, commit your changes and open a pull request.


### Colab notebook
Click here to get started writing a tutorial in Colab:
[New Colab tutorial](https://colab.research.google.com/github/google/earthengine-community/blob/master/tutorials/tutorial-template.ipynb)
This will open a notebook containing instructions for authoring and submitting your tutorial.
### Advanced
If you're already familiar with GitHub, git, and related tools, the overall process is the same for submitting both Markdown and Colab tutorials:
  1. Fork and clone the [google/earthengine-community](https://github.com/google/earthengine-community) GitHub repository.
  2. Create a directory under `tutorials` with the slugified short name of your tutorial (e.g., `tutorials/my-amazing-tutorial`).
  3. Add the appropriate header for [Markdown](https://developers.google.com/earth-engine/tutorials/community/styleguide#markdown) or [Colab](https://developers.google.com/earth-engine/tutorials/community/styleguide#colab).
  4. Commit the tutorial to the new directory with the filename `index.md` (for Markdown) or `tutorial.ipynb` (for Colab). Commit images used in the tutorial to the same directory.
  5. Push the new content to your fork and [open a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork).


When creating a pull request, be sure to refer to the original proposal by its GitHub issue number in the comment section. For example, if the issue was #123, you would place the text "Closes #123" in the pull request description to reference the original proposal, and to automatically mark it as done once the tutorial is published.
Once you've opened a pull request, one or more maintainers will be assigned to review your submission. The reviewer(s) will work with you to ensure your submission is complete, correct, and that it is consistent with the [Earth Engine Community Tutorial Style Guide](https://developers.google.com/earth-engine/tutorials/community/styleguide).
Once your pull request is approved, your tutorial will be published by the repository maintainers.
