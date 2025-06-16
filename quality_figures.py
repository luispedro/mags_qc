from os import makedirs
import polars as pl
import seaborn as sns
from matplotlib import pyplot as plt


makedirs('./plots', exist_ok=True)

qs = pl.read_csv('./checkm2_output/quality_report.tsv',
                    separator='\t')

fig,axes = plt.subplots(2, 2,
                        sharex='col', sharey='row',
                        width_ratios=[.9, .1], height_ratios=[.1, .9])
sns.histplot(data=qs, x='Completeness', binwidth=.2, ax=axes[0,0], )
sns.histplot(data=qs, y='Contamination', binwidth=.2, ax=axes[1,1], )
axes[1,0].scatter(qs['Completeness'], qs['Contamination'], s=2, alpha=.5)
axes[0,1].set_visible(False)
axes[1,0].set_xlabel('Completeness')
axes[1,0].set_ylabel('Contamination')
sns.despine(fig, trim=True)
fig.tight_layout()
plt.savefig('plots/quality_scatter_with_histograms.svg', bbox_inches='tight')
