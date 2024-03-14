using System.Runtime.CompilerServices;

public class Fraction
{
    private int _topCDN;
    private int _bottomCDN;


    public Fraction()
    {
        _topCDN = 1;
        _bottomCDN = 1;
    }

    public Fraction(int WholeNumber)
    {
        _topCDN = WholeNumber;
        _bottomCDN = 1;
    }

    public Fraction(int top, int bottom)
    {
        _topCDN = top;
        _bottomCDN = bottom;
    }
    public string GetFractionStringCDN()
    {
        string text = $"{_topCDN}/{_bottomCDN}";
        return text;
    }
    public double GetDecimalValueCDN()
    {
        return (double)_topCDN / (double)_bottomCDN;
    }
}