from os import makedirs
import polars as pl
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import cm


makedirs('./plots', exist_ok=True)

qs = pl.read_csv('./checkm2_output/quality_report.tsv',
                    separator='\t')

fig,axes = plt.subplots(3, 2,
                        width_ratios=[.9, .1], height_ratios=[.1, .85, .05],)
sns.histplot(data=qs, x='Completeness', binwidth=.2, ax=axes[0,0], )
sns.histplot(data=qs, y='Contamination', binwidth=.2, ax=axes[1,1], )
s = axes[1,0].scatter(
        qs['Completeness'],
        qs['Contamination'],
        s=8,
        alpha=.5,
        c=qs['Total_Contigs'],
        cmap=cm.viridis)
axes[0,1].set_visible(False)
axes[2,1].set_visible(False)
axes[1,0].set_xlabel('Completeness')
axes[1,0].set_ylabel('Contamination')
fig.colorbar(s, cax=axes[2,0], orientation='horizontal')
axes[2,0].set_xlabel('Nr of contigs')
sns.despine(fig, trim=True)
fig.tight_layout()
fig.savefig('plots/quality_scatter_with_histograms.svg', bbox_inches='tight')

fig,ax = plt.subplots()
ax.scatter(qs['Average_Gene_Length'], 100*qs['Coding_Density'])
ax.set_ylabel('Coding density (%)')
ax.set_xlabel('Average gene length (aa)')
sns.despine(fig, trim=True)
fig.tight_layout()
fig.savefig('plots/average_gene_length_vs_coding_density.svg', bbox_inches='tight')


