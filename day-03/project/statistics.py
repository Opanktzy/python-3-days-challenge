# statistics.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict
from models import Student

class StatisticsAnalyzer:
    """Class untuk analisis statistik dengan NumPy, Pandas, dan Matplotlib"""

    def __init__(self, students: List[Student]):
        self.students = students
        self.df = self._create_dataframe()

    def _create_dataframe(self) -> pd.DataFrame:
        """Buat DataFrame dari data student"""
        if not self.students:
            return pd.DataFrame()

        data = [student.to_dict() for student in self.students]
        return pd.DataFrame(data)

    def show_basic_stats(self):
        """Tampilkan statistik dasar dengan Pandas"""
        if self.df.empty:
            print("⚠️ Tidak ada data untuk dianalisis")
            return

        print("\n" + "="*60)
        print("📊 STATISTIK DASAR")
        print("="*60)
        print("\n📌 Statistik Numerik:")
        print(self.df[['age', 'grade']].describe())

        print("\n📌 Distribusi Gender:")
        print(self.df['gender'].value_counts())

        print("\n📌 Distribusi Major:")
        print(self.df['major'].value_counts())

    def analyze_with_numpy(self) -> Dict:
        """Analisis dengan NumPy"""
        if not self.students:
            return {}

        ages = np.array([s.age for s in self.students])
        grades = np.array([s.grade for s in self.students])

        return {
            'age_stats': {
                'mean': np.mean(ages),
                'median': np.median(ages),
                'std': np.std(ages),
                'min': np.min(ages),
                'max': np.max(ages)
            },
            'grade_stats': {
                'mean': np.mean(grades),
                'median': np.median(grades),
                'std': np.std(grades),
                'min': np.min(grades),
                'max': np.max(grades)
            }
        }

    def create_visualizations(self):
        """Buat visualisasi dengan Matplotlib"""
        if self.df.empty:
            print("⚠️ Tidak ada data untuk divisualisasi")
            return

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('📊 Visualisasi Data Student', fontsize=16, fontweight='bold')

        # 1. Distribusi Usia
        axes[0, 0].hist(self.df['age'], bins=10, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Distribusi Usia')
        axes[0, 0].set_xlabel('Usia')
        axes[0, 0].set_ylabel('Jumlah')

        # 2. Distribusi Grade
        grade_counts = self.df['grade'].value_counts().sort_index()
        axes[0, 1].bar(grade_counts.index, grade_counts.values, color='lightcoral')
        axes[0, 1].set_title('Distribusi Grade')
        axes[0, 1].set_xlabel('Grade')
        axes[0, 1].set_ylabel('Jumlah')

        # 3. Distribusi Gender
        gender_counts = self.df['gender'].value_counts()
        axes[1, 0].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
        axes[1, 0].set_title('Distribusi Gender')

        # 4. Major Distribution
        major_counts = self.df['major'].value_counts().head(5)
        axes[1, 1].barh(major_counts.index, major_counts.values, color='lightgreen')
        axes[1, 1].set_title('Top 5 Major')
        axes[1, 1].set_xlabel('Jumlah')

        plt.tight_layout()
        plt.show()

    def get_advanced_stats(self) -> pd.DataFrame:
        """Dapatkan statistik lanjutan dengan Pandas"""
        if self.df.empty:
            return pd.DataFrame()

        # Group by major untuk analisis
        grouped = self.df.groupby('major').agg({
            'age': ['mean', 'min', 'max'],
            'grade': ['mean', 'min', 'max']
        })
        return grouped
