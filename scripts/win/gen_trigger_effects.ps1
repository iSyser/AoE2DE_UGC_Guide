$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/scenarios/triggers/effects"
python effects.py
Pop-Location
