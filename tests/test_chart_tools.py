# -*- utf-8 -*-

from base64 import b64encode
import plotly.express as px
import numpy as np

from unittest import TestCase

from tools.chart_tools import ChartTools


class TestChartTools(TestCase):
    def setUp(self):
        self.tool = ChartTools()
        self.figure = self.build_figure()

    def build_figure(self):
        np.random.seed(1)
        x, y, sz, cl = np.random.rand(4, 100)
        return px.scatter(x=x, y=y, size=sz, color=cl)

    def test_to_base64(self):
        """
        it should convert a given plotly figure to base64 encode
        """
        img_bytes = self.figure.to_image(format="png")
        encoding = b64encode(img_bytes).decode()
        img_b64 = "data:image/png;base64," + encoding

        self.assertEqual(img_b64, self.tool.to_base64(self.figure))
