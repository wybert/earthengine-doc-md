 
#  Community Tutorial Style Guide
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://developers.google.com/earth-engine/tutorials/community/styleguide#overview)
  * [General guidelines](https://developers.google.com/earth-engine/tutorials/community/styleguide#general_guidelines)
  * [Tutorial file headers](https://developers.google.com/earth-engine/tutorials/community/styleguide#tutorial_file_headers)
  * [Tutorial templates](https://developers.google.com/earth-engine/tutorials/community/styleguide#tutorial_templates)


## Overview
This guide provides general guidelines for writing your own Google Earth Engine tutorials. It aims to make it easy to create high-quality tutorials that are clear, concise, and easily understood by the entire Earth Engine community.
The [tutorial templates](https://developers.google.com/earth-engine/tutorials/community/styleguide#tutorial_templates) below double as an additional guide to help kickstart your own tutorials. Details on how to use the templates to get started can be found in [Writing a Tutorial](https://developers.google.com/earth-engine/tutorials/community/write).
In addition, the [Google Cloud Platform Community Tutorial Style Guide](https://cloud.google.com/community/tutorials/styleguide) provides a valuable reference for writing end-to-end tutorials for a broad audience, while the [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html) details the recommended style for use in JavaScript code samples. Reviewers may refer to these guides when reviewing your submission.
## General guidelines
  * Be brief.
  * Don't repeat yourself. 
    * Don't say the same thing twice (even if worded differently).
  * Periodically mark progress. 
    * Include images and text at key points in the tutorial so the user knows they're on track. Use sparingly!
  * Use the active voice whenever possible. 
    * "When the user changes the value", not "when the value is changed".
    * Exception: It's okay to use passive voice when you'd have to go out of your way to use active voice, or if the actor is obvious or not relevant ("an animated GIF is returned" instead of "Earth Engine returns an animated GIF").
  * Stick to the facts. 
    * Avoid superlatives ("this is **_100%_** the **_best_** and **_fastest_** method").
    * Avoid promoting products or services.
    * Avoid controversial topics.
    * Include citations and URLs when referencing specific methods, datasets, and analyses.
  * Make your tutorial self-contained. 
    * Try not to rely on special libraries outside the API or datasets not in the public [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/).
    * If you're providing additional data or algorithms, only share them if you have permission to do so. Include all required licenses and attributions.
  * Test your code. 
    * Be sure to run and test all included code samples right before submitting your article for review.


## Tutorial file headers
If you're creating and submitting community tutorials manually without using the templates provided in [Writing a Tutorial](https://developers.google.com/earth-engine/tutorials/community/write), you'll need to manually add the appropriate metadata and license header to the start of the file. Select the desired format to view a template which can be copied into your own tutorial:
[Markdown](https://developers.google.com/earth-engine/tutorials/community/styleguide#markdown)[Colab](https://developers.google.com/earth-engine/tutorials/community/styleguide#colab) More
Add the following to the beginning of the document. No whitespace or other characters should precede the header:
```
---
title: Your tutorial title
description: A short description of the tutorial, all on one line with no carriage returns.
author: your-github-username
tags: comma-separated, lowercase, list, of, related, keywords
date_published: YYYY-MM-DD
---
<!--
Copyright 2023 The Google Earth Engine Community Authors
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

```

Be sure to replace the appropriate template fields before submitting your tutorial for review.
Add the following to a code cell at the beginning of the notebook:
```
#@title Copyright 2023 The Earth Engine Community Authors { display-mode: "form" }
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

```

## Tutorial templates
[Markdown](https://developers.google.com/earth-engine/tutorials/community/styleguide#markdown)[Colab](https://developers.google.com/earth-engine/tutorials/community/styleguide#colab) More
If you're familiar with git and GitHub, you may use the code below as a template to get you started:
```
---
title: Your tutorial title
description: A short description of the tutorial, all on one line with no carriage returns.
author: your-github-username
tags: comma-separated, lowercase, list, of, related, keywords
date_published: YYYY-MM-DD
---
<!--
Copyright 2023 The Google Earth Engine Community Authors
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
In a few sentences, describe what the user is going to learn. Be sure to include
_concise_ background information; only include what's helpful and relevant.
When in doubt, leave it out!
## Section heading 1
Break up your tutorial into manageable sections.
With one or more paragraphs, separated by a blank line.
Inside your sections, you can also:
1. Use numbered lists
1. ..when the order..
1. ..of items is important.
And:
- This is a bulleted list.
- Use bulleted lists when items are not strictly ordered.
..and even:
Use   | tables  | to organize | content
------- | -------- | ----------- | -------
Your  | tables  | can     | also
contain | multiple | rows    | ...
## Section heading 2
Use separate sections for related, but discrete, groups of steps.
Use code blocks to show users how to do something after describing it:
```js
// Use comments to describe details that can't be easily expressed in code.
// Always try making code more self descriptive before adding a comment.
// Similarly, avoid repeating verbatim what's already said in code
// (e.g., "assign ImageCollection to variable 'coll'").
var coll = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA');
```
### Use subsections if appropriate
Consider breaking longer sections that cover multiple topics or span multiple
pages into subsections.

```

Alternatively, the above template can be opened directly in GitHub's web based file editor by following instructions at [Writing a Tutorial](https://developers.google.com/earth-engine/tutorials/community/write).
Be sure to refer to [Writing a Tutorial](https://developers.google.com/earth-engine/tutorials/community/write) for important details on how to propose, author, and submit tutorials.
To create a new Colab notebook using the recommended style template, click here:
[New Colab tutorial](https://colab.research.google.com/github/google/earthengine-community/blob/master/tutorials/tutorial-template.ipynb)
This will open a notebook containing instructions for authoring and submitting your tutorial. Be sure to refer to [Writing a Tutorial](https://developers.google.com/earth-engine/tutorials/community/write) for important details on the proposal, authoring, and submission process.
