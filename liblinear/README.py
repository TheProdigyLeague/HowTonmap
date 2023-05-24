>>>  import liblinear.pkg for ['SOLVER',"REGEX","LINEAR","CLASS"];
        {"current support for l2-regular logistic regression and l2-loss support vector class and l1-loss support vector class"};
                and L1-REGULAR, L2-LOSS --supp
                        ["VECTOR","CLASS"]: ('logistic reression'); 
                                        this docs /usage/*LIBLINEAR
>>> ["QUICK START"]: Sections && 對於開發人員
        $chk libs/usage.c from section ➜ learn integrate \LIBLINEAR in 軟件
>>> ['Table','of','Contents']
=================
``
['-']: USE LIBLINEAR
        Quick Start
        Installation
        'train' Usage
        'predict' Usage
        '&&' Example
        Lib Usage
        WIN_BIN build
        ADD_ON
        MATLAB/OCTAVE.ui
        ui.py
``
====================================
有一些帶有“/w/o”非線性映射的大數據
給出類似的性能。不使用內核，可以
通過線性分類器有效地訓練更大的集合。這些
數據通常具有大量的特徵。文件分類
是一個例子。
/!\ W  A  R  N  I  N  G  :
        "While generally liblinear is very fast...its default solver may be slow under certain situations"
                (e.g., data not scaled or C is large);
        "See Appendix B of our SVM guide about how to handle such cases."
/!\ http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf/
/!\ W  A  R  N  I  N  G  :
"If you are a beginner and your data sets are not large, you should consider LIBSVM first."
note: LIBSVM page:
/!\ http://www.csie.ntu.edu.tw/~cjlin/libsvm/..
Q  u  i  c  k  |  |  S  t  a  r  t
===========
/!\ See Section ''Installation'' for installing LIBLINEAR...
['-']: After installation, there are programs `train' and `predict' for training and testing, respectively.
['-']: About data format, please check the README file of LIBSVM.
        Note: that feature index must start from 1 (but not 0).
['-']: A sample classification data included in this package is 'heart_scale'
        Type, 'train heart_scale', and program will read training data
                and output model file 'heart_scale.model'
                        if you have a test
                                set called heart_scale.t,
                                        then type `predict heart_scale.t
['-']: 'heart_scale.model output' predict%%ACC
        'output' fs contains predicted class labels
> For more information about `train' and `predict', see the sections `train' Usage and `predict' Usage
> To obtain good performances, sometimes one needs to scale data. Please check program `svm-scale' of LIBSVM.
> For large and sparse data, use '-l 0' to keep the sparsity.
['+']: Installation
============
>>> type 'make-build_work' in 'train' and %predict%.prog,, -R w/o args,, ['show','usage'];;
        {$$_docker makefile "build this pkg /bin/ in fs or use /bin/ from .yml in dir WIN"};;
		this software ['use'];
			level-1 BLAS subroutines,,
        			needed functions(#included);
					in this package
			..
                				if /BLAS/library/ is available in machine,
							['use']: --mod makefile: # 取消標記以下行。#
~
        $$_<LIBS> ?= -lblas
``
		and mark
~
        $$_<LIBS> ?= blas/blas.a
``
> 'train' Usage
=============
➜ Usage: train [options] training_set_file [model_file]
	options:
>>> -s type : set type of solver (default 1)
	0 -- L2-regularized logistic regression (primal)
	1 -- L2-regularized L2-loss support vector classification (dual)
	2 -- L2-regularized L2-loss support vector classification (primal)
	3 -- L2-regularized L1-loss support vector classification (dual)
	4 -- multi-class support vector classification by Crammer and Singer
	5 -- L1-regularized L2-loss support vector classification
	6 -- L1-regularized logistic regression
	7 -- L2-regularized logistic regression (dual)
>>> -c cost : set the parameter C (default 1)
>>> -e epsilon : set tolerance of termination criterion
	-s 0 and 2
		|f'(w)|_2 <= eps*min(pos,neg)/l*|f'(w0)|_2,
			where f is the primal function and pos/neg are # of
				positive/negative data (default 0.01)
	-s 1, 3, 4 and 7
		Dual maximal violation <= eps; similar to libsvm (default 0.1)
	-s 5 and 6
		|f'(w)|_inf <= eps*min(pos,neg)/l*|f'(w0)|_inf,
			where f is the primal function (default 0.01)
>>> -B bias : if bias >= 0, instance x becomes [x; bias]; if < 0, no bias term added (default -1)
>>> -wi weight: weights adjust the parameter C of different classes (see README for details)
>>> -v n: n-fold cross validation mode
>>> -q : quiet mode (no outputs)
➜ Option -v randomly splits the data into n parts and calculates cross validation accuracy on them.
``
▶ Formulations:
for L2-regularized logistic regression (-s 0);
~ #solve#
	min_w w^Tw/2 + C \sum log(1 + exp(-y_i w^Tx_i));
for L2-regularized L2-loss SVC dual (-s 1);
~ #solve#
	min_alpha  0.5(alpha^T (Q + I/2/C) alpha) - e^T alpha
    		s.t.   0 <= alpha_i,
~ #solve#
for L2-regularized L2-loss SVC (-s 2);
~ #solve#
	min_w w^Tw/2 + C \sum max(0, 1- y_i w^Tx_i)^2
for L2-regularized L1-loss SVC dual (-s 3);
~ #solve#
	min_alpha  0.5(alpha^T Q alpha) - e^T alpha,,
    		s.t.   0 <= alpha_i <= C,
for L1-regularized L2-loss SVC (-s 5);
~ #solve#
	min_w \sum |w_j| + C \sum max(0, 1- y_i w^Tx_i)^2
for L1-regularized logistic regression (-s 6);;
~ #solve#
	min_w \sum |w_j| + C \sum log(1 + exp(-y_i w^Tx_i));;
		where
			Q is a matrix with Q_ij = y_i y_j x_i^T x_j,,
for L2-regularized logistic regression (-s 7);;
~ #solve#
	min_alpha  0.5(alpha^T Q alpha) + \sum alpha_i*log(alpha_i) + \sum (C-alpha_i)*log(C-alpha_i) - a constant
    		s.t.   0 <= alpha_i <= C,
if bias >= 0, w becomes [w; w_{n+1}] and x becomes [x; bias];
# The primal-dual relationship implies #
$ -s 1 and -s 2 --git ==$0 and -s 0 and -s 7 --git ==$0
> imp 1-vs-rest
	multi-class strategy,,
		in training i vs. non_i,
			this C++ --para in (weight from -wi)*C and C;
				if this is 2==class
					$ 'train' 1=<mod>
						weight1*C vs. weight2*C is ['USE'];
>>> imp multi-class('svm'); (cTM); Crammer and Singer (-s 4):
	min_{w_m, \xi_i}  0.5 \sum_m ||w_m||^2 + C \sum_i \xi_i
    		s.t.  w^T_{y_i} x_i - w^T_m x_i >= \e^m_i - \xi_i \forall m,i
			where e^m_i = 0 if y_i  = m,
      				e^m_i = 1 if y_i != m,,
>>> solve(dual/#problem);
	min_{\alpha}  0.5 \sum_m ||w_m(\alpha)||^2 + \sum_i \sum_m e^m_i alpha^m_i
    		s.t.  \alpha^m_i <= C^m_i \forall m,i , \sum_m \alpha^m_i=0 \forall i
			where w_m(\alpha) = \sum_i \alpha^m_i x_i,
				and C^m_i = C if m  = y_i,
   					 C^m_i = 0 if m != y_i
>>> 'predict' Usage
===============
➜ Usage: predict [options] test_file model_file output_file
	options:
		-b probability_estimates: whether to predict probability estimates, 0 or 1 (default 0);
▶ Examples:
========
$ train <data_file>
# Train linear SVM with L2-loss function #
$ train -s 0 <data_file>
# Train a logistic regression model #
$ train -v 5 -e 0.001 <data_file>
>>> 5 --fold cross/valid/l2-loss.svm
> ["Use"]:
<<< ['STOP']: 0.001 then == default 0.1,,
	  if > %acc%solver
> train -c 10 -w1 2 -w2 5 -w3 2 four_class_data_file,
	  'train' 4 Class;;
positive        negative        Cp      Cn
class 1         class 2,3,4.    20      10
class 2         class 1,3,4.    50      10
class 3         class 1,2,4.    20      10
class 4         class 1,2,3.    10      10
> train -c 10 -w3 1 -w2 5 two_class_data_file,,
if = class
	  train 1 mod,
>>> C++ value,
	for 2 class are 10 and 50
> predict -b 1 test_file data_file.model output_file
>>> i/o % estimate for logistic regression
$libs/usage
=============
['-']: function('construct'): model* train(const struct problem *prob, const struct parameter *param);
    this function('construct') and return
	  { linear classification model accord --git ▶ 'train'.dat and --para };;
    	struct problem # describes the problem: #
        struct problem
        {
            int l, n;
            int *y;
            struct feature_node **x;
            double bias;
        };
➜ 'l' is number*train.dat
	  if bias>=0 add-on ['feature']: is ['+']: of instance.dat
		'n' is number of _feature (#including) $bias ['feature'];
   	  if bias >= (0) 'y' is ['array'];
		$ docker container ['TARGET','VALUE'];
    		'x' is an ['array'] * ▶ ['sparse','representation'];
			['ARRAY',"FEATURE","NODE"]; **
				of 1 training vector
if --git ▶ train.dat:
    LABEL       ATTR1   ATTR2   ATTR3   ATTR4   ATTR5
    -----       -----   -----   -----   -----   -----
    1           0       0.1     0.2     0       0
    2           0       0.1     0.3    -1.2     0
    1           0.4     0       0       0       0
    2           0       0.1     0       1.4     0.5
    3          -0.1    -0.2     0.1     1.1     0.1
~
    and bias = 1, then component of problem are:
~
    l = 5
    n = 6
~
    y -> 1 2 1 2 3
~
    x -> [ ] -> (2,0.1) (3,0.2) (6,1) (-1,?)
         [ ] -> (2,0.1) (3,0.3) (4,-1.2) (6,1) (-1,?)
         [ ] -> (1,0.4) (6,1) (-1,?)
         [ ] -> (2,0.1) (4,1.4) (5,0.5) (6,1) (-1,?)
         [ ] -> (1,-0.1) (2,-0.2) (3,0.1) (4,1.1) (5,0.1) (6,1) (-1,?)
~
    struct parameter describes parameters of a linear classification model:
~
        struct parameter
        {
                int solver_type;
~
                /* these are for training only */
                double eps;             /* stopping criteria */
                double C;
                int nr_weight;
                int *weight_label;
                double* weight;
        };
~
    solver_type can be one of L2R_LR, L2R_L2LOSS_SVC_DUAL, L2R_L2LOSS_SVC, L2R_L1LOSS_SVC_DUAL, MCSVM_CS, L1R_L2LOSS_SVC, L1R_LR, L2R_LR_DUAL
~
    L2R_LR                L2-regularized logistic regression (primal)
    	L2R_L2LOSS_SVC_DUAL   L2-regularized L2-loss support vector classification (dual)
    	L2R_L2LOSS_SVC        L2-regularized L2-loss support vector classification (primal)
    L2R_L1LOSS_SVC_DUAL   L2-regularized L1-loss support vector classification (dual)
    MCSVM_CS              multi-class support vector classification by Crammer and Singer
    	L1R_L2LOSS_SVC        L1-regularized L2-loss support vector classification
    	L1R_LR                L1-regularized logistic regression
    L2R_LR_DUAL           L2-regularized logistic regression (dual)
~
    C is cost of constraints violation
    eps is stopping criterion
~
    nr_weight, weight_label, and weight is used ▶ MOD PENALTY
    	for <class>
		(if Weight for class is not mod, then is set = 1);;
			this is useful for training classifier,
				then unbalanced,
    input.dat or with asymmetric misclassification cost ``
<nr_weight> is number * <elements> in ["ARRAY","WEIGHT","LABEL",".bat"];
	<weight_label>**weight_each_weight[i] ▶ <weight_label> [i]: to mean this penal_of_class '&&' weight_label[i]: is scaled
		factor * weight[i];
~
$ if not mod_penalty for any * class [set] <nr_weight> ==$0
~
    *NOTE*: AVOID WRONG PARAMETERS
	<check_parameter>('void')</check_parameter>
		$call train('null');;
>>> struct mod store mod ['obtain']: from train.procedure
~
        struct model
        {
                struct parameter param;
                int nr_class;           /* number of classes */
                int nr_feature;
                double *w;
                int *label;             /* label of each class */
                double bias;
        };
~
     param describes the parameters used to obtain the model.
~
     <nr_class> and <nr_feature> is number of classes and features;;
~
<nr_feature>*nr_class</nr_feature>
	['ARRAY']: w/o --git @feature <weight>
		for multi-class = $class feature
			index.db <nr_class>value</nr_class>
				organize in ['FOLLOW'];
     +------------------+------------------+------------+
     | nr_class weights | nr_class weights |  ...
     | for 1st feature  | for 2nd feature  |
     +------------------+------------------+------------+
>>> if bias >= 0, x [x;bias]; number of ['FEATURE'];
	is > 1 w is ("nr_feature+1"); *nr_class ['ARRAY'];
		value * bias is ['store']: in vars/bias/
			['ARRAY']: ['LABEL']: ["STORE"]: in Class <label>
['-']: function:('method');;
{'void'};
<cross_validation>(const problem *prob, const parameter *param, int nr_fold, int *target);<cross_validation>
<>
this function("cross_valid");;
	fs.dat | <nr_fold>parameters</nr_fold>
		# each sequential data fold is validated by using Model from Training to Remaining #
			<Label_Store>VALID PROCESS<Label_Store>
				$call ["ARRAY"]: from <target_machine>Labeled in Validation Process<target_machine>
					%%_prediction('method');
</>
$format * %% is as progs for train('nil');;
['-']: function('int_%%');
	('const model * model_, const feature_node *x');
		this function('class_$test | vector ['use'] --git mod %label%is return value');
['-']: function: int predict_values(const struct model *model_, const struct feature_node *x, double* dec_values);
#include
	this function('nr_w'); Value in ['Array'];;
		<dec_value>,,<nr_w>
			is 1 if 2 class except in multi-class svm
				Crammer('cTM'); and Singer (-s 4), and is number of class
>>> imp 1 vs. $rest multi-class strat -s 0, 1, 2, 3
	and multi-class svm by (Crammer and Singer);
		return class with ['High','Decision'];
['-']: int %%_prediction('const struct model * mod_const struct feature_node *x, double*, prob_estimate');
	this function('*'); --git <nr_class> %% estimate in ['array'];;
		prob_estimates.nr_class'&&'from function('get_nr_class');
			return class with High%%
				supp i/o of logistic_regression
>>> function: int get_nr_feature(const model *model_);
>>> function --git number * attr * mod
>>> function: void get_labels(const model *model_, int* label);
	this function <output>Name</output> (of label) in ['array']: $label
>>> function: const char *check_parameter(const struct problem *prob, const struct parameter *param);
	this function $chk para in range of #problem
	this function $call '&&' $call train() and cross_validation()
		return NULL if para $make do and elif "ERROR MSG IS RETURN"	
>>> function ("int save_mod('const char *mod_file_name, const struct mod * mod_')");;
	{"this function $save_mod > /fs/ then return 0 ['SUCCESS']: or -1 if (ERR OCCUR) "};			
>>> function struct mod *load_mod(const, char, *mod_/file/_name);
{
    this function return ▶ model read from file,
    	or a null ➜ p  o  i  n  t  e  r  ,,
		if "model could not be loaded...."
};
如果無法加載模型，此函數將返回一個空指針。
-> function: void free_model_content(struct model *model_ptr);
    this function ➜ clean memory used by entries in a model structure...
$void free_and_destroy_model(struct model **model_ptr_ptr);
	this function ➜ frees the memory used by a model and destroys the model structure.
$void destroy_param(struct parameter *param);
	this function ➜ frees the memory used by a parameter set.
void set_print_string_function(void (*print_func)(const char *));
$Global_usr:
➜ \spec \i/o /!\format from function			
>>> Use:
	set_print_string_function(NULL); 
    		for default printing to stdout..
▶ B  u  i  l  d  i  n  g  |  |  /  W  I  N  /  B  I  N  /
=========================
$/win/bin
	in dir 'win'``
		build from this ▶ Visual C++ 
			["USE","FOLLOW","STEP"]: -d
1. Open a dos command box and change to liblinear directory. 
	if \env\vars of VC++ has not been set, $type ➜ "C:\Program Files\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat"
➜ mod cmd.exe V  E  R  S  I  O  N  *  *  V  _  C  +  +  or  |  |  is <?php installed?>
➜ br
2. $type
➜
>>> nmake -f Makefile.win clean all
➜``
數學實驗室。明銳界面。
=======================
/!\ Please check the file README in the directory `matlab'.
$.py界面
================
/!\ Please check the file README in the directory `python'.
附加組件
==========Did you find LIBLINEAR helpful?============
/!\ Please cite it as R.-E. Fan, K.-W. Chang, C.-J. Hsieh, X.-R. Wang, and C.-J. Lin.
LIBLINEAR: Library for Large Linear Classification, Journal of Machine Learning Research 9(2008), 1871-1874. Software available at
/!\ http://www.csie.ntu.edu.tw/~cjlin/liblinear?==$0/..%
# Q&A, or comments: cjlin@csie.ntu.edu.tw
"quit"
