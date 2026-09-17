from pathlib import Path
import tarfile,json
root=Path(__file__).parent
manifest=json.loads((root/'.openai/hosting.json').read_text())
assert manifest['static']['directory']=='dist'
archive=root/'miria-site.tar.gz'
with tarfile.open(archive,'w:gz') as tar:
    tar.add(root/'dist',arcname='dist')
    tar.add(root/'.openai/hosting.json',arcname='dist/.openai/hosting.json')
with tarfile.open(archive) as tar:
    names=tar.getnames()
    assert 'dist/index.html' in names and 'dist/.openai/hosting.json' in names
    assert not any(x.startswith('/') or '..' in Path(x).parts for x in names)
    print(json.dumps({'archive':str(archive),'files':len(names),'bytes':archive.stat().st_size}))
