---
title: Writing documentation
status: draft
toc: True
toc_sticky: True
tags: [template]
---

This page shows some of the Markdown and Liquid widgets that are available for writing documentation using this template. The Markdown file used to create this page can be viewed [on GitHub](https://github.com/adamancer/knowledge-hub-template/blob/main/collections/_how-to-guides/writing-documentation.md).

## Heading 2

Headings provide the basic structure to a page. HTML supports six levels of headings. The top-level heading is added automatically based on the page title. Among other things, headings are used to make pages accessible, so always use them in order and don't use bold, italtics, or underline to signify a heading!

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

## Formatting text

**Bold** or *italics* can make a word or phrase stand out.

## Lists

Unordered lists use bullets:

- Unordered
- List

Ordered lists use numbers:

1. Ordered
1. List

## Tables

| Col 1        | Col 2        | Col 3        |
|--------------|--------------|--------------|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |
| Row 3, Col 1 | Row 3, Col 2 | Row 3, Col 3 |

## Notices

{:.notice}
**Notices** can be used to make information stand out.

{:.notice--info}
**Information notices** highlight important information.

{:.notice--warning}
**Warnings** let users know about potential problems or gotchas.

## Links

[Jekyll relative links]({{ '/' | relative_url }}) use URLs relative to the site root

{% include private_link text='Private links' url='#' %} may require additional authentication

{% include external_link text='External links' url='#' %} take users to another site
