using System.Drawing;

public abstract class Shape
{
    private string _colorCDN;

    public Shape(string color)
    {
        _colorCDN = color;
    }

    public string GetColor()
    {
        return _colorCDN;
    }

    public void SetColor(string color)
    {
        _colorCDN = color;
    }
    
    public abstract double GetArea();
}
