# -*- utf-8 -*-

from base64 import b64encode


class ChartTools:
    """
    Class designed to handle chart operations
    """

    def check_figure(self, figure):
        """
        Method used to check the given figure

        :param figure: Plotly figure
        :type figure: plotly.graph_object.Figure

        :raises: AttributeError

        """
        if figure is None:
            raise AttributeError("The figure cannot be empty")

    def to_base64(self, figure):
        """
        Method used to transform a Plotly figure into a base64 encoded image string

        :param figure: Plotly figure
        :type figure: plotly.graph_object.Figure

        :return: str -- Encoded figure as a base64 string

        """
        img_bytes = figure.to_image(format="png")
        encoding = b64encode(img_bytes).decode()
        return "data:image/png;base64," + encoding
