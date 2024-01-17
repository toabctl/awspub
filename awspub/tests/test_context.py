import pathlib

from awspub import context


curdir = pathlib.Path(__file__).parent.resolve()


def test_context_create():
    """
    Create a Context object from a given configuration
    """
    ctx = context.Context(curdir / "fixtures/config1.yaml", None)
    assert ctx.conf["source"]["path"] == curdir / "fixtures/config1.vmdk"
    assert ctx.source_sha256 == "6252475408b9f9ee64452b611d706a078831a99b123db69d144d878a0488a0a8"
    assert ctx.conf["source"]["architecture"] == "x86_64"
    assert ctx.conf["s3"]["bucket_name"] == "bucket1"
    assert ctx.conf["s3"]["bucket_region"] == "region1"


def test_context_create_minimal():
    """
    Create a Context object from a given minimal configuration
    """
    ctx = context.Context(curdir / "fixtures/config-minimal.yaml", None)
    assert ctx.conf["source"]["path"] == curdir / "fixtures/config1.vmdk"
    assert ctx.source_sha256 == "6252475408b9f9ee64452b611d706a078831a99b123db69d144d878a0488a0a8"
    assert ctx.conf["source"]["architecture"] == "x86_64"
    assert ctx.conf["s3"]["bucket_name"] == "bucket1"
    assert ctx.conf["s3"]["bucket_region"] == "eu-central-2"


def test_context_create_with_mapping():
    """
    Create a Context object from a given configuration
    """
    ctx = context.Context(curdir / "fixtures/config2.yaml", curdir / "fixtures/config2-mapping.yaml")
    assert ctx.conf["source"]["path"] == curdir / "fixtures/config1.vmdk"
    assert ctx.source_sha256 == "6252475408b9f9ee64452b611d706a078831a99b123db69d144d878a0488a0a8"
    assert ctx.conf["images"].get("test-image-value1")
    assert ctx.conf["images"].get("test-image-value$2")
