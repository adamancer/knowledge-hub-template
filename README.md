# Knowledge Hub Template

This repository contains files for a template knowledge hub based on the 
[minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) Jekyll theme and
the [Divio Documentation System](https://docs.divio.com/documentation-system/).

### Writing front matter

Open the Markdown file and add the *front matter*, which is a special section at the 
top of each Markdown document with metadata about the page. Front matter is 
delineated by a line of three hyphens before and after the content. The content itself
is written in YAML, a human-readable markup language.

The front matter should include:

- The **title** of the page
- The publication **status** of the page. Pages with `status: published` are
  considered complete. Pages with any other status will include a warning that the
  page is still in draft form.
- The **last_modified_at** date as `yyyy-mm-dd`
- Associated **tags** as a list. In YAML, lists are comma-delimited and use square
  brackets.

Other metadata (for example, page layouts and navigation) are added automatically
based on the section the page appears in.

Metadata for the file `writing-documentation.md` might look like this:

```yaml
---
title: Writing documentation
status: draft
last_modified_at: 2025-04-21
topics: [documentation]
---
```

### Writing content

Individual pages are written in Markdown, which is a simple, readable syntax used to
format text documents. Content can be added below the front matter. A cheat
sheet for Markdown is available [here](https://www.markdownguide.org/cheat-sheet/).

Markdown files can also include HTML. HTML should be used sparingly and only when
suitable Markdown is not available, for example, for embed tags.

Jekyll also supports [Liquid](https://shopify.github.io/liquid/), which is a template
language that can be used to add dynamic content to pages. Liquid tags should also be
used sparingly, with the primary exceptions being (1) use of the `relative_url`
filter to link to pages elsewhere on the site and (2) use of `include` tags to display
widgets defined by either the `minimal-mistakes` template or created specifically for
this site.

#### Linking within the site

We recommend using Jekyll's `relative_url` filter to link to other pages on the hub.
This filter accepts a root-relative URL. Note that the collections folder is not
part of the URL for pages in a collection and that page names do not need to include
a file extension.

Link to a top-level page:

```
[Tutorials]{{ "/tutorials" | relative_url }}
```

Link to a page in a collection:

```
[Getting started]{{ "/tutorials/getting-started" | relative_url }}
```

#### Widgets

Include a list of related pages matching one or more topics:

```
{% include related_list topics='manage data|share data' %}
```

Include a 
[callout box](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/#notices):

```
{: .notice--info }
**Callout**
Here's some important info.
```

## Building the site

It can be useful to build the site locally before submitting a pull request or
committing changes to the main repository. The build process uses a combination of
Python and Ruby to index the site, update metadata for external resources, and build
HTML pages from the Markdown files.

Note that files created during the build process are not committed to GitHub. The build
process runs automatically through a GitHub Action when changes are pushed to the
repository.

### Initial setup

Building the site locally requires the following three applications:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [MiniForge](https://github.com/conda-forge/miniforge) (under Install)
- [Ruby](https://www.ruby-lang.org/en/downloads) (under Ways of Installing Ruby)

Once those applications are installed, you can create a new repository under your
account based on the template and clone it to your system.

```
git clone https://github.com/{username}/repo-name
```

Navigate to the directory you just created:

```
cd path/to/repo-name
```

Set up the Python environment:

```
mamba create -f environment.yml
```

Set up Jekyll:

```
gem install bundler jekyll
```

### Build the site locally

Open the command prompt and run the following commands to activate the environment
needed to build and run the site locally:

```
mamba activate kh
cd path/to/knowledge-hub
```

To build the site and launch Jekyll, run the following commands in the same prompt:

```
cd scripts
python build-site.py
cd ..
bundle exec jekyll serve
```

Alternatively you can simply run Jekyll itself:

```
bundle exec jekyll serve
```

Jekyll will pick up many routine changes as files are updated, but some changes
(including but not limited to changes to _config.yml or tag lists on individual
pages) will not be reflected until Jekyll is restarted or the full site is rebuilt.

## Acknolwedgments

Icons are from the [Remix icon set](https://icon-sets.iconify.design/ri/) (Apache 2.0)
from Iconify. 
