---
title: Tags
nav_order: 5
layout: faceted
facet_data: tags
facet_keys: [tags]
sidebar:
  nav: [sidebar]
  collapsible: True
---

<table class="faceted">
  <tr><th>Resource</th><th>Section</th></tr>
  {% for item in site.data[page.facet_data] %}
    {% assign segments = item.url | split: "/" %}
    <tr data-tags="{{ item.tags | join: '|'}}">
      <td><a {% if item.kind == 'external' %}class="external" {% endif %}href="{% if item.kind == 'external' %}{{ item.url }}{% else %}{{ item.url | relative_url}}{% endif %}">{{ item.title }}</a></td>
      <td>{{ segments[1] | capitalize | replace: "-to", " to" | replace: "-guides", " guides" }}</td>
    </tr>
  {% endfor %}
</table>