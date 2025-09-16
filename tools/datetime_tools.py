from datetime import datetime
from zoneinfo import ZoneInfo

from agno.tools.toolkit import Toolkit


class DateTimeTools(Toolkit):
    """Ferramentas de datas/horas."""

    def __init__(self, **kwargs) -> None:
        """Inicializa a ferramenta de datas/horas.

        Args:
            **kwargs: Parâmetros adicionais para a inicialização da ferramenta.
        """
        super().__init__(
            name='datetime_tools',
            tools=[
                self.get_current_time,
                self.get_current_date,
                self.get_current_date_and_time,
                self.get_day_of_week,
            ],
            **kwargs,
        )

    @staticmethod
    def __now() -> datetime:
        """Retorna o momento atual, em formato datetime,
        considerando o fuso do fuso horário 'America/Sao_Paulo'.

        Returns:
            datetime: o momento atual
        """
        return datetime.now(ZoneInfo('America/Sao_Paulo'))

    def get_current_time(self) -> str:
        """Retorna a string com a hora atual,
        no formato '%H:%M' + 'h', ex: '14:30h'.

        Returns:
            str: a string com a hora atual
        """
        return self.__now().strftime('%H:%M' + 'h')

    def get_current_date(self) -> str:
        """Retorna uma string com a data atual,
        no formato '%d/%m/%Y', ex: '25/12/2022'.

        Returns:
            str: a string com a data atual
        """
        return self.__now().strftime('%d/%m/%Y')

    def get_current_date_and_time(self) -> str:
        """Retorna uma string com a data e hora atuais,
        no formato '%d/%m/%Y %H:%M' + 'h', ex: '25/12/2022 14:30h'.

        Returns:
            str: a string com a data e hora atuais
        """
        return self.__now().strftime('%d/%m/%Y %H:%M' + 'h')

    def get_day_of_week(self) -> str:
        """Retorna uma string com o dia da semana atual,
        no formato '%A', ex: 'Quarta-feira'.

        Returns:
            str: a string com o dia da semana atual
        """
        return self.__now().strftime('%A')
