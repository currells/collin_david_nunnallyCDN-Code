using System.Diagnostics;

public class Square : Shape
{
    private double _sideCDN;

    public Square(string color, double side) : base (color)
    {
        _sideCDN = side;
    }

    public override double GetArea()
    {
        return _sideCDN * _sideCDN;
    }
}