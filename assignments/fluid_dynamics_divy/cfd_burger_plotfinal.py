import numpy
from matplotlib import pyplot, cm, use
from matplotlib.colors import Normalize
use("agg")

class Burgers:

   def __init__(self, Lx, Ly, nx, ny):
      self.Lx = Lx  # starting inputs
      self.Ly = Ly
      self.nx = nx
      self.ny = ny
      # setup necessary variables
      self.sigma = 0.001
      self.nu = 0.01
      self.bv = 0  # boundary condition
      self.nt = 2510  # number of steps to simulate
      self.dx = Lx / float(self.nx - 1)
      self.dy = Ly / float(self.ny - 1)
      self.dt = self.sigma * self.dx * self.dy / self.nu
      self.u = numpy.ones(shape=(ny, nx))
      self.v = numpy.ones(shape=(ny, nx))
      self.nozzle_u = numpy.append(10 * numpy.ones(1000), numpy.zeros(self.nt))  # nozzle special boundary conditions
      self.nozzle_v = numpy.append(10 * numpy.ones(1000), numpy.zeros(self.nt))
      # evolve for nt amount to obtain the final matrices
      self.evolve()
      #self.equation_of_motion()

   def set_boundary_conditions(self, t_step):
      self.u[0, :] = self.bv  # set 0th index of each row to bv
      self.u[-1, :] = self.bv  # set last index of each row to bv
      self.u[:, 0] = self.bv  # set 0th index of each column to bv
      self.u[:, -1] = self.bv  # set last index of each column to bv
      # repeat for y-component matrix
      self.v[0, :] = self.bv
      self.v[-1, :] = self.bv
      self.v[:, 0] = self.bv
      self.v[:, -1] = self.bv
      # special nozzle boundary conditions
      self.u[self.ny//2-2:self.ny//2+2, 0] = self.nozzle_u[t_step]
      self.v[self.ny//2-2:self.ny//2+2, 0] = self.nozzle_v[t_step]
      return True

   def equation_of_motion(self):
      un = self.u.copy()
      vn = self.v.copy()
      self.u[1:-1, 1:-1] = un[1:-1, 1:-1] - self.dt/self.dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) - self.dt/self.dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) + self.nu * self.dt / self.dy**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) + self.nu * self.dt / self.dx**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])
      self.v[1:-1, 1:-1] = vn[1:-1, 1:-1] - self.dt/self.dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) - self.dt/self.dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) + self.nu * self.dt / self.dy**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) + self.nu * self.dt / self.dx**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])
      return True

   def evolve(self):
      for i in range(0, self.nt, 1):
         self.equation_of_motion()
         self.set_boundary_conditions(i)
      return True

   def display(self):
      print(self.u)
      print("\n")
      print(self.v)
   
   def fetch_u(self):
      return self.u
   
   def fetch_v(self):
      return self.v

def run():
   cfd = Burgers(2, 2, 5, 5)
   u = cfd.fetch_u()
   v = cfd.fetch_v()
   ax = pyplot.figure()
   norm = Normalize()
   magnitude = numpy.sqrt(u[::2]**2 + v[::2]**2)
   pyplot.quiver(u[::2], v[::2], norm(magnitude), scale=60, cmap=pyplot.cm.jet)
   ax.savefig('frame'+str(50).zfill(5)+'.png',dpi=300)
   ax.clear()
   return True