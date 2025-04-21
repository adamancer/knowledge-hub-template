---
title: Explanations
status: draft
nav_order: 3
sidebar:
  nav:
  - sidebar
  collapsible: true
  expanded:
  - explanations
---

A landing page for documents explaining a system or process.

<h2>Pages</h2>
<ul>
{% for item in site.explanations %}
{% unless item.parent %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endunless %}
{% endfor %}
</ul>