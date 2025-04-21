---
title: How To Guides
status: draft
nav_order: 2
sidebar:
  nav:
  - sidebar
  collapsible: true
  expanded:
  - how-to-guides
---

A landing page for documents that provide instructions for how to accomplish a specific task.

<h2>Pages</h2>
<ul>
{% for item in site["how-to-guides"] %}
{% unless item.parent %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endunless %}
{% endfor %}
</ul>