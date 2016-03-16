# -*- coding: utf-8 -*-

'''
Copyright 2016 Randal S. Olson

This file is part of the TPOT library.

The TPOT library is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

The TPOT library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
the TPOT library. If not, see http://www.gnu.org/licenses/.
'''

pipeline_seeds = ['_random_forest(ARG0, mul(100, 5), 0)',
                  '_xgradient_boosting(ARG0, 0.1, mul(100, 5), 3)',
                  '_logistic_regression(ARG0, 1.0)',
                  '_decision_tree(ARG0, 1, 0)',
                  '_knnc(ARG0, 5)',
                  '_random_forest(_xgradient_boosting(ARG0, 0.1, mul(100, 5), 3), mul(100, 5), 0)',
                  '_random_forest(_logistic_regression(ARG0, 1.0), mul(100, 5), 0)',
                  '_logistic_regression(_polynomial_features(ARG0), 1.0)',
                  '_random_forest(_polynomial_features(ARG0), mul(100, 5), 0)',
                  '_random_forest(_select_percentile(ARG0, 10), mul(100, 5), 0)',
                  '_decision_tree(_xgradient_boosting(ARG0, 0.1, mul(100, 5), 3), 1, 0)',
                  '_random_forest(_random_forest(ARG0, mul(100, 5), 0), mul(100, 5), 0)',
                  '_logistic_regression(_random_forest(ARG0, mul(100, 5), 0), 1.0)',
                  '_logistic_regression(_logistic_regression(ARG0, 1.0), 1.0)',
                  '_random_forest(_pca(ARG0, 5, 3), mul(100, 5), 0)',
                  '_logistic_regression(_xgradient_boosting(ARG0, 0.1, mul(100, 5), 3), 1.0)',
                  '_xgradient_boosting(_logistic_regression(ARG0, 1.0), 0.1, mul(100, 5), 3)',
                  '_random_forest(_select_fwe(ARG0, 0.05), mul(100, 5), 0)',
                  '_random_forest(_knnc(ARG0, 5), mul(100, 5), 0)',
                  '_xgradient_boosting(_polynomial_features(ARG0), 0.1, mul(100, 5), 3)',
                  '_logistic_regression(_knnc(ARG0, 5), 1.0)',
                  '_xgradient_boosting(_select_percentile(ARG0, 10), 0.1, mul(100, 5), 3)',
                  '_logistic_regression(_select_percentile(ARG0, 10), 1.0)',
                  '_xgradient_boosting(_xgradient_boosting(ARG0, 0.1, mul(100, 5), 3), 0.1, mul(100, 5), 3)',
                  '_xgradient_boosting(_knnc(ARG0, 5), 0.1, mul(100, 5), 3)',
                  '_logistic_regression(_select_fwe(ARG0, 0.05), 1.0)',
                  '_knnc(_random_forest(ARG0, mul(100, 5), 0), 5)',
                  '_decision_tree(_random_forest(ARG0, mul(100, 5), 0), 1, 0)',
                  '_logistic_regression(_decision_tree(ARG0, 1, 0), 1.0)',
                  '_random_forest(_decision_tree(ARG0, 1, 0), mul(100, 5), 0)',
                  '_decision_tree(_decision_tree(ARG0, 1, 0), 1, 0)',
                  '_decision_tree(_logistic_regression(ARG0, 1.0), 1, 0)',
                  '_knnc(_logistic_regression(ARG0, 1.0), 5)',
                  '_decision_tree(_knnc(ARG0, 5), 1, 0)',
                  '_xgradient_boosting(_random_forest(ARG0, mul(100, 5), 0), 0.1, mul(100, 5), 3)',
                  '_decision_tree(_select_percentile(ARG0, 10), 1, 0)',
                  '_xgradient_boosting(_select_fwe(ARG0, 0.05), 0.1, mul(100, 5), 3)',
                  '_decision_tree(_polynomial_features(ARG0), 1, 0)',
                  '_knnc(_xgradient_boosting(ARG0, 0.1, mul(100, 5), 3), 5)',
                  '_knnc(_decision_tree(ARG0, 1, 0), 5)',
                  '_logistic_regression(_standard_scaler(ARG0), 1.0)',
                  '_xgradient_boosting(_pca(ARG0, 5, 3), 0.1, mul(100, 5), 3)',
                  '_random_forest(_rfe(ARG0, 5, 1.0), mul(100, 5), 0)',
                  '_xgradient_boosting(_decision_tree(ARG0, 1, 0), 0.1, mul(100, 5), 3)',
                  '_logistic_regression(_rfe(ARG0, 5, 1.0), 1.0)',
                  '_decision_tree(_pca(ARG0, 5, 3), 1, 0)',
                  '_knnc(_knnc(ARG0, 5), 5)',
                  '_knnc(_select_percentile(ARG0, 10), 5)',
                  '_random_forest(_select_fwe(_polynomial_features(ARG0), 0.05), mul(100, 5), 0)',
                  '_logistic_regression(_select_fwe(_polynomial_features(ARG0), 0.05), 1.0)',
                  '_xgradient_boosting(_select_fwe(_polynomial_features(ARG0), 0.05), 0.1, mul(100, 5), 3)']
