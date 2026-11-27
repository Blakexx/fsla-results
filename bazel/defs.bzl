"""fsla-results' wrappers of fsla-devtools' generic rules (the doc references among them): each handed this workspace's
environment (`results_env`) and tracked tree."""

load("@results_env//:flags.bzl", "VENV")
load("@results_tree//:tree.bzl", "TRACKED")
load("@fsla_devtools//bazel:rules.bzl", _docrefs_test = "docrefs_test", _tool_run = "tool_run", _tree_part = "tree_part",
     _tree_test = "tree_test")

def tree_test(**kwargs):
    """A check over the tree's tracked files, the environment's tools on PATH."""
    _tree_test(venv = VENV, **kwargs)

def tree_part(parts = {}):
    """This package's part of the tree: `tracked` and `tracked_python`."""
    _tree_part(TRACKED, parts)

def results_run(**kwargs):
    """A module of the checkout run by `bazel run` in it, on the environment's interpreter: its arguments follow `--`."""
    _tool_run(venv = VENV, environment = True, **kwargs)

def docrefs_test(**kwargs):
    """The doc references (fsla-devtools' `fsla_devtools.docrefs`), on the environment's interpreter, in the checkout."""
    _docrefs_test(python = Label("@results_env//:python"), tool = Label("@docrefs//:docrefs.py"),
                  anchor = Label("//:MODULE.bazel"), **kwargs)
