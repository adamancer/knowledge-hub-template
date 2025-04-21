"""Creates and indexes pages based using YAML files in _data"""

import yaml

from const import BASEPATH
from utils import (
    autolink,
    build_nav,
    compute_urls,
    index_tags,
    read_fms,
    to_slug,
    write_fm,
)

if __name__ == "__main__":

    with open(BASEPATH / "_config.yml") as f:
        config = yaml.safe_load(f).get("python")

    # Construct the navigation and build a tag index using file front matter. This
    # section should generally not be modified.

    print("Reading front matter")
    fms = read_fms(BASEPATH)

    print("Determining URLs")
    compute_urls(fms)

    print("Indexing tags")
    index_tags(fms, config["tag_name"])

    print("Building navigation")
    build_nav(fms, include_main=config["main_nav"])
