from src.facturacion.reportes import generar_factura

def test_factura_simple():
    total = generar_factura([2, 1], [50, 100])  # subtotal = 200
    assert total == 242.0  # con IVA 21%

def test_factura_con_descuento():
    total = generar_factura([2], [100], descuento=10)
    assert total == 217.8  # 200 -10% +21%