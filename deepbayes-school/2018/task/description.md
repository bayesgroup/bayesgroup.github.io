<h2 align="center">Practical Assignment DeepBayes 2018</h2> 

The strong knowledge of math, programming, and the ability to do research have become the most important skills in machine learning. 
In this task, we address unsupervised learning, a very fundamental AI problem. 
More specifically, we suggest you to implement Fully Connected Autoencoder using PyTorch for dimensionality reduction, and optionally to do some research with this model. 

We define Autoencoder as two parametric differentiable functions, namely the Encoder (E) and the Decoder(D). Parameters of these two functions are adjusted by minimization of the following loss function:
<center>
  <div>
    <img src="http://ars-ashuha.ru/images/eq.png" align="middle" width="640"> 
  </div>
</center>
where the left part is L2 reconstruction loss, the right part is L1 regularizer, and λ is a scalar regularizer weight.  

You are requested to implement the AutoEncoder class. 
Use [ ```task.py```](https://bayesgroup.github.io/deepbayes-school/2018/task/task.py) as a template of the solution; all technical details are described there. 
Your solution has to be implemented in _python 3.6_ with _PyTorch(torch==0.3.0)_.
Changing prototypes of the functions and using additional libraries (except included) is prohibited, otherwise, the solution will be automatically rejected.
Please copy to the form only the implementation of the AutoEncoder class.

**UPD 1:** In your solution λ may be equal to 0 since we define loss as a static method and it is hard to get parameters from it. The research part does not put any restrictions on the interface, so you can change it.
**UPD 2:** We have changed the interface of the solution a little bit -- AutoEncoder.loss_function is not a static method anymore. So you can easily implement your l1 regularizer. Both version of the solution (with static method e.g. λ=0 or without) will be accepted. Apologise for that :).


In the optional research assignment, we ask you to study:

- Which reconstruction loss and regularizer lead to more natural images?
- How different parameters of your architecture influence the solution? For example, consider a different number of layers and a number of neurons. Is it beneficial to use noisy layers like Dropout?

We suggest you to check the solution via ```test_work``` function. 
Please, note that ```test_work``` checks only interfaces, but does not check whether the solution is correct.
