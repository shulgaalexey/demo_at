Write-Output "AT UP"
Start-Process -FilePath "python" -ArgumentList ".\1esbot_app.py" -NoNewWindow
Start-Process -FilePath "python" -ArgumentList ".\icm_wrp_mock.py" -NoNewWindow
Start-Process -FilePath "python" -ArgumentList ".\knowledge_svc_mock.py" -NoNewWindow