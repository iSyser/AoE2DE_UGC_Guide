$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/scenarios/triggers/conditions"
python conditions.py
Pop-Location
