Sub StockVBA2():
Dim Ticker As String
Dim TotalVol As Double
Dim YearChange As Double
Dim PercentChange As Double
Dim SumVol As Integer
Dim OpenValue As Double
Dim CloseValue As Double
For Each ws In Worksheets
    TotalVol = 0
    SumVol = 2
    ws.Range("I1") = "Ticker"
    ws.Range("J1") = "Yearly Change"
    ws.Range("K1") = "Percent Change"
    ws.Range("L1") = "Total Stock Volume"
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    OpenValue = ws.Cells(2, 3)
    For i = 2 To LastRow
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            Ticker = Cells(i, 1).Value
            TotalVol = TotalVol + Cells(i, 7).Value
            CloseValue = Cells(i, 6).Value
            YearChange = CloseValue - OpenValue
            If OpenValue = 0 Then
                PercentChange = 0
            Else
                PercentChange = YearChange / OpenValue * 100
           End If
            ws.Range("I" & SumVol).Value = Ticker
            ws.Range("J" & SumVol).Value = YearChange
            ws.Range("K" & SumVol).Value = (PercentChange & "%")
            ws.Range("L" & SumVol).Value = TotalVol
            TotalVol = 0
            OpenValue = ws.Cells(i + 1, 3)
             If ws.Range("J" & SumVol).Value >= 0 Then
                ws.Range("J" & SumVol).Interior.ColorIndex = 4
            Else
                ws.Range("J" & SumVol).Interior.ColorIndex = 3
                End If
                SumVol = SumVol + 1
        Else
            TotalVol = TotalVol + ws.Cells(i, 7)
        End If
    Next i

Next ws

End Sub