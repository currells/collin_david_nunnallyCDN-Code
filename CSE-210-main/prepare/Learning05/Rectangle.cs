public class Rectangle : Shape
{
    private double _lengthCDN;
    private double _widthCDN;

    public Rectangle(string color, double length, double width) : base (color)
    {
        _lengthCDN = length;
        _widthCDN = width;
    }

    public override double GetArea()
    {
        return _lengthCDN * _widthCDN;
    }
}