Invoke-Sqlcmd -ServerInstance 192.168.1.1 -Database DatabaseName -Query "select * from ItemTable" -Username "sa" -Password "sa" -MaxCharLength 9970000 | Format-Table -Wrap -AutoSize| Out-File -Width 500 -Encoding utf8 -filePath "C:\Temp\Item.xml"

(Get-Content C:\Temp\Item.xml -raw).Replace('
Column1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
-------                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
', '') | Set-Content C:\Temp\Item.xml
 
Invoke-Sqlcmd -ServerInstance 192.168.1.1 -Database DatabaseName -Query "select * from StockTable" -Username "sa" -Password "sa" -MaxCharLength 9970000 | Format-Table -Wrap -AutoSize| Out-File -Width 500 -Encoding utf8 -filePath "C:\Temp\Stock.xml"
 
 
 (Get-Content C:\Temp\Stock.xml -raw).Replace('
Column1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
-------                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
', '') | Set-Content C:\Temp\Stock.xml



  # Load WinSCP .NET assembly
  Add-Type -Path "C:\WinSCP\WinSCPnet.dll"

  # Setup session options
  $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
    Protocol = [WinSCP.Protocol]::Ftp
    HostName = "IP Address"
    UserName = "Username"
    Password = "Password"

  }

  $session = New-Object WinSCP.Session

  try
  {
      # Connect
      $session.Open($sessionOptions)

      # Upload Items
      $session.PutFiles("C:\Temp\Item.xml", "/documents/xml/").Check()

      # Upload Stock
      $session.PutFiles("C:\Temp\Stock.xml", "/documents/xml/").Check()
  }
  finally
  {
      # Disconnect, clean up
      $session.Dispose()
  }