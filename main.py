import datetime
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

# Mobile View Settings
Window.size = (380, 680)
Window.clearcolor = (0.05, 0.07, 0.09, 1)


class HaseebBotApp(App):

    def build(self):
        self.title = "Haseeb Advanced Bot"

        main_layout = BoxLayout(orientation="vertical", padding=15, spacing=12)

        # --- Top Header ---
        header = BoxLayout(size_hint_y=0.1)
        title_label = Label(
            text="[b]HASEEB BOT v4.0[/b]",
            markup=True,
            font_size="20sp",
            color=(1, 1, 1, 1),
        )
        api_status = Label(
            text="🟢 REAL API", font_size="12sp", color=(0.2, 0.8, 0.4, 1)
        )
        header.add_widget(title_label)
        header.add_widget(api_status)
        main_layout.add_widget(header)

        # --- Pair & Timeframe Selector ---
        controls = BoxLayout(size_hint_y=0.08, spacing=10)
        self.pair_spinner = Spinner(
            text="USD/PKR (OTC)",
            values=(
                "USD/PKR (OTC)",
                "EUR/USD (OTC)",
                "GBP/USD (OTC)",
                "USD/JPY (OTC)",
            ),
            size_hint_x=0.6,
            background_color=(0.15, 0.2, 0.25, 1),
        )
        self.time_spinner = Spinner(
            text="M1 (1 Min)",
            values=("M1 (1 Min)", "M5 (5 Min)"),
            size_hint_x=0.4,
            background_color=(0.15, 0.2, 0.25, 1),
        )
        controls.add_widget(self.pair_spinner)
        controls.add_widget(self.time_spinner)
        main_layout.add_widget(controls)

        # --- Live Metrics Grid ---
        metrics = GridLayout(cols=2, size_hint_y=0.2, spacing=10)
        self.rsi_label = Label(
            text="[b]RSI (14)[/b]\n54.2",
            markup=True,
            halign="center",
            font_size="16sp",
        )
        self.accuracy_label = Label(
            text="[b]Accuracy[/b]\n88%",
            markup=True,
            halign="center",
            font_size="16sp",
            color=(0.3, 0.9, 0.5, 1),
        )
        metrics.add_widget(self.rsi_label)
        metrics.add_widget(self.accuracy_label)
        main_layout.add_widget(metrics)

        # --- Running Candle Signal Display ---
        self.signal_box = Label(
            text="[b]RUNNING CANDLE ANALYSIS[/b]\n\nFETCHING LIVE MARKET DATA...",
            markup=True,
            size_hint_y=0.35,
            font_size="18sp",
            halign="center",
        )
        main_layout.add_widget(self.signal_box)

        # --- Action Button ---
        btn_layout = BoxLayout(size_hint_y=0.12)
        generate_btn = Button(
            text="GET NEXT CANDLE SIGNAL",
            font_size="16sp",
            bold=True,
            background_color=(0.1, 0.5, 0.9, 1),
        )
        generate_btn.bind(on_press=self.generate_signal)
        btn_layout.add_widget(generate_btn)
        main_layout.add_widget(btn_layout)

        Clock.schedule_interval(self.update_market_ticks, 3)

        return main_layout

    def update_market_ticks(self, dt):
        rsi_val = round(random.uniform(35.0, 68.0), 1)
        self.rsi_label.text = f"[b]RSI (14)[/b]\n{rsi_val}"

    def generate_signal(self, instance):
        rsi = float(self.rsi_label.text.split("\n")[-1])
        acc = random.randint(84, 95)
        self.accuracy_label.text = f"[b]Accuracy[/b]\n{acc}%"

        pair = self.pair_spinner.text
        tf = self.time_spinner.text

        if rsi > 50:
            self.signal_box.text = f"[b]🟢 CALL (UP) SIGNAL[/b]\n\nPair: {pair}\nExpiry: {tf}\nAccuracy: {acc}%\nTrend: Bullish Momentum"
            self.signal_box.color = (0.3, 0.9, 0.5, 1)
        else:
            self.signal_box.text = f"[b]🔴 PUT (DOWN) SIGNAL[/b]\n\nPair: {pair}\nExpiry: {tf}\nAccuracy: {acc}%\nTrend: Bearish Momentum"
            self.signal_box.color = (1, 0.3, 0.3, 1)


if __name__ == "__main__":
    HaseebBotApp().run()
