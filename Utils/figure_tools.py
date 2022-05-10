from matplotlib import pyplot as plt
from labellines import labelLine, labelLines


def make_sens_spec_figs(main_tb, err_tb, WHICH='') :
    

    fig, ax = plt.subplots(1, 3, figsize=[15,5])


    ax[1].errorbar(main_tb['Sensitivity'], main_tb['PPV at prevalence of 5 percent'], 
                 yerr=err_tb['PPV at prevalence of 5 percent'], capsize=2, label='5%',
                 color='c', linestyle='-', alpha=0.7)

    ax[1].errorbar(main_tb['Sensitivity'], main_tb['PPV at prevalence of 10 percent'], 
                 yerr=err_tb['PPV at prevalence of 10 percent'], capsize=2, label='10%',
                 color='c', linestyle='-', alpha=0.7)

    ax[1].errorbar(main_tb['Sensitivity'], main_tb['PPV at prevalence of 20 percent'], 
                 yerr=err_tb['PPV at prevalence of 20 percent'], capsize=2, label='20%',
                 color='c', linestyle='-', alpha=0.7)

    ax[1].errorbar(main_tb['Sensitivity'], main_tb['PPV at prevalence of 30 percent'], 
                 yerr=err_tb['PPV at prevalence of 30 percent'], capsize=2, label='30%',
                 color='c', linestyle='-', alpha=0.7)

    ax[1].errorbar(main_tb['Sensitivity'], main_tb['PPV at prevalence of 40 percent'], 
                 yerr=err_tb['PPV at prevalence of 40 percent'], capsize=2, label='40%',
                 color='c', linestyle='-', alpha=0.7)

    ax[1].errorbar(main_tb['Sensitivity'], main_tb['PPV at prevalence of 50 percent'], 
                 yerr=err_tb['PPV at prevalence of 50 percent'], capsize=2, label='50%',
                 color='c', linestyle='-', alpha=0.7)

    labelLines(ax[1].get_lines(),align=False,fontsize=10)


    ##########################################################################################################

    ax[2].errorbar(main_tb['Sensitivity'], main_tb['NPV at prevalence of 5 percent'], 
                 yerr=err_tb['NPV at prevalence of 5 percent'], capsize=2, label='5%',
                 color='r', linestyle='-', alpha=0.7)

    ax[2].errorbar(main_tb['Sensitivity'], main_tb['NPV at prevalence of 10 percent'], 
                 yerr=err_tb['NPV at prevalence of 10 percent'], capsize=2, label='10%',
                 color='r', linestyle='-', alpha=0.7)

    ax[2].errorbar(main_tb['Sensitivity'], main_tb['NPV at prevalence of 20 percent'], 
                 yerr=err_tb['NPV at prevalence of 20 percent'], capsize=2, label='20%',
                 color='r', linestyle='-', alpha=0.7)

    ax[2].errorbar(main_tb['Sensitivity'], main_tb['NPV at prevalence of 30 percent'], 
                 yerr=err_tb['NPV at prevalence of 30 percent'], capsize=2, label='30%',
                 color='r', linestyle='-', alpha=0.7)

    ax[2].errorbar(main_tb['Sensitivity'], main_tb['NPV at prevalence of 40 percent'], 
                 yerr=err_tb['NPV at prevalence of 40 percent'], capsize=2, label='40%',
                 color='r', linestyle='-', alpha=0.7)

    ax[2].errorbar(main_tb['Sensitivity'], main_tb['NPV at prevalence of 50 percent'], 
                 yerr=err_tb['NPV at prevalence of 50 percent'], capsize=2, label='50%',
                 color='r', linestyle='-', alpha=0.7)

    labelLines(ax[2].get_lines(),align=False,fontsize=10)


    ax[0].errorbar(main_tb['Sensitivity'], main_tb['Specificity'], yerr=err_tb['Specificity'], capsize=2, 
                 label='specificity', color='k')

    ax[0].set_xlabel('model sensitivity')
    ax[1].set_xlabel('model sensitivity')
    ax[2].set_xlabel('model sensitivity')


    ax[0].set_title('Specificity');
    ax[1].set_title('PPV at varied prevalences');
    ax[2].set_title('NPV at varied prevalences');

    #ax[1].legend()
    #ax[2].legend()
    #plt.title(WHICH + ' task performance vs. model sensitivity (holdout set)');
    ax[0].axis([0.05,.95,0.0,1.05])
    ax[1].axis([0.05,.95,0.0,1.05])
    ax[2].axis([0.05,.95,0.0,1.05])

    if len(WHICH) :
        fig.suptitle(WHICH + ' Task Performance vs. Model Sensitivity (holdout set)', fontweight="bold");

    ax[0].text(.07,1.07,'a', fontsize='16', fontweight='bold')
    ax[1].text(.07,1.07,'b', fontsize='16', fontweight='bold')
    ax[2].text(.07,1.07,'c', fontsize='16', fontweight='bold')


    #plt.savefig('sens_spec_prev_' + WHICH + '.tiff', dpi=300, facecolor='white')