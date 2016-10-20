def get_lpx_d_all(X, F, B, s):
##################################################################
#
# Calculates log(p(X_k|d_k,F,B,s)) for all images X_k in X and 
# all possible displacements d_k.
#
# Input parameters:
#
#   X ... H x W x N numpy.array, N images of size H x W
#   F ... h x w numpy.array, estimate of villain's face
#   B ... H x W numpy.array, estimate of background
#   s ... 1 x 1, estimate of standart deviation of Gaussian noise
#
# Output parameters:
#   
#   lpx_d_all ... (H-h+1) x (W-w+1) x N numpy.array, 
#                 lpx_d_all[dh,dw,k] - log-likelihood of 
#                 observing image X_k given that the villain's 
#                 face F is located at displacement (dh, dw)
#
##################################################################

	
def calc_L(X, F, B, s, A, q, useMAP = False):
###################################################################
#
# Calculates the lower bound L(q,F,B,s,A) for the marginal log 
# likelihood
#
# Input parameters:
#
#   X ... H x W x N numpy.array, N images of size H x W
#   F ... h x w numpy.array, estimate of villain's face
#   B ... H x W numpy.array, estimate of background
#   s ... 1 x 1, estimate of standart deviation of Gaussian noise
#   A ... (H-h+1) x (W-w+1) numpy.array, estimate of prior on 
#         displacement of face in any image
#   q  ... if useMAP = False:
#             (H-h+1) x (W-w+1) x N numpy.array, 
#             q[dh,dw,k] - estimate of posterior of displacement 
#             (dh,dw) of villain's face given image Xk
#           if useMAP = True:
#             2 x N numpy.array, 
#             q[0,k] - MAP estimates of dh for X_k 
#             q[1,k] - MAP estimates of dw for X_k 
#   useMAP ... logical, if true then q is a MAP estimates of 
#              displacement (dh,dw) of villain's face given image 
#              Xk 
#
# Output parameters:
#   
#   L ... 1 x 1, the lower bound L(q,F,B,s,A) for the marginal log 
#         likelihood
#
###################################################################

	
def e_step(X, F, B, s, A, useMAP = False):
##################################################################
#
# Given the current esitmate of the parameters, for each image Xk
# esitmates the probability p(d_k|X_k,F,B,s,A)
#
# Input parameters:
#
#   X ... H x W x N numpy.array, N images of size H x W
#   F ... h x w numpy.array, estimate of villain's face
#   B ... H x W numpy.array, estimate of background
#   s ... 1 x 1, estimate of standart deviation of Gaussian noise
#   A ... (H-h+1) x (W-w+1) numpy.array, estimate of prior on 
#         displacement of face in any image
#   useMAP ... logical, if true then q is a MAP estimates of 
#              displacement (dh,dw) of villain's face given image 
#              Xk 
#
# Output parameters:
#   
#   q  ... if useMAP = False:
#             (H-h+1) x (W-w+1) x N numpy.array, 
#             q[dh,dw,k] - estimate of posterior of displacement 
#             (dh,dw) of villain's face given image Xk
#           if useMAP = True:
#             2 x N numpy.array, 
#             q[0,k] - MAP estimates of dh for X_k 
#             q[1,k] - MAP estimates of dw for X_k 
###################################################################

	
def m_step(X, q, h, w, useMAP = False):
###################################################################
# 
# Estimates F,B,s,A given esitmate of posteriors defined by q
#
# Input parameters:
#
#   X ... H x W x N numpy.array, N images of size H x W
#   q ... if useMAP = False:
#             (H-h+1) x (W-w+1) x N numpy.array, 
#             q[dh,dw,k] - estimate of posterior of displacement 
#             (dh,dw) of villain's face given image Xk
#           if useMAP = True:
#             2 x N numpy.array, 
#             q[0,k] - MAP estimates of dh for X_k 
#             q[1,k] - MAP estimates of dw for X_k 
#   h ... 1 x 1, face mask hight
#   w ... 1 x 1, face mask widht
#  useMAP ... logical, if true then q is a MAP estimates of 
#             displacement (dh,dw) of villain's face given image 
#             Xk 
#
# Output parameters:
#   
#   F ... h x w numpy.array, estimate of villain's face
#   B ... H x W numpy.array, estimate of background
#   s ... 1 x 1, estimate of standart deviation of Gaussian noise
#   A ... (H-h+1) x (W-w+1) numpy.array, estimate of prior on 
#         displacement of face in any image
###################################################################

	
def run_EM(X, h, w, F=None, B = None, s = None, A = None,
    tolerance = 0.001, max_iter = 50, useMAP = False):
###################################################################
# 
# Runs EM loop until the likelihood of observing X given current
# estimate of parameters is idempotent as defined by a fixed 
# tolerance
#
# Input parameters:
#
#   X ... H x W x N numpy.array, N images of size H x W
#   h ... 1 x 1, face mask hight
#   w ... 1 x 1, face mask widht
#   F, B, s, A ... initial parameters (optional!)
#   F ... h x w numpy.array, estimate of villain's face
#   B ... H x W numpy.array, estimate of background
#   s ... 1 x 1, estimate of standart deviation of Gaussian noise
#   A ... (H-h+1) x (W-w+1) numpy.array, estimate of prior on 
#         displacement of face in any image
#   tolerance ... parameter for stopping criterion
#   max_iter  ... maximum number of iterations
#   useMAP ... logical, if true then after E-step we take only 
#              MAP estimates of displacement (dh,dw) of villain's 
#              face given image Xk 
#    
#
# Output parameters:
#   
#   F, B, s, A ... trained parameters
#   LL ... 1 x (number_of_iters + 2) numpy.array, L(q,F,B,s,A) 
#          at initial guess, after each EM iteration and after 
#          final estimate of posteriors;
#          number_of_iters is actual number of iterations that was 
#          done
###################################################################
    


def run_EM_with_restarts(X, h, w, tolerance = 0.001, max_iter = 50,
                     useMAP = False, restart=10):
###################################################################
# 
# Restarts EM several times from different random initializations 
# and stores the best estimate of the parameters as measured by 
# the L(q,F,B,s,A)
#
# Input parameters:
#
#   X ... H x W x N numpy.array, N images of size H x W
#   h ... 1 x 1, face mask hight
#   w ... 1 x 1, face mask widht
#   tolerance, max_iter, useMAP ... parameters for EM
#   restart   ... number of EM runs
#
# Output parameters:
#   
#   F ... h x w numpy.array, the best estimate of villain's face
#   B ... H x W numpy.array, the best estimate of background
#   s ... 1 x 1, the best estimate of standart deviation of 
#         Gaussian noise
#   A ... (H-h+1) x (W-w+1) numpy.array, the best estimate of 
#         prior on displacement of face in any image
#   LL ... 1 x 1, the best L(q,F,B,s,A)
###################################################################



