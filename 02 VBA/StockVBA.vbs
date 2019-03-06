Sub StockVBA()
Dim Ticker As String
Dim TotalVol As Double
Dim SumVol As Integer
For Each ws In Worksheets
    TotalVol = 0
    SumVol = 2
    ws.Range("I1") = "Ticker"
    ws.Range("J1") = "Total Stock Volume"
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    For i = 2 To LastRow
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            Ticker = Cells(i, 1).Value
            TotalVol = TotalVol + Cells(i, 7).Value
            ws.Range("I" & SumVol).Value = Ticker
            ws.Range("J" & SumVol).Value = TotalVol
            SumVol = SumVol + 1
            TotalVol = 0
        Else
            TotalVol = TotalVol + ws.Cells(i, 7)
        End If
    Next i

Next ws

End Sub