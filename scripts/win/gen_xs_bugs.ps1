$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/xs/bugs"
python bugs.py
Pop-Location
