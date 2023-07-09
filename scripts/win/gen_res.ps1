$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/general/resources"
python resources.py
Pop-Location
